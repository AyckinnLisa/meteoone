import os, requests, json, pathlib
from datetime import datetime

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtGui import QPixmap

from meteoone_window import Ui_MeteoOne


os.system('clear')

basedir = pathlib.Path(__file__).parent.absolute()


'''
    Get and save JSON datas from the API in JSON file
'''
def update_json_file():
    api_link = "https://api.openweathermap.org/data/2.5/weather?q=castelnau-le-lez&lang=fr&appid=738e9d1489491771d579f8b5db5fd21a"

    json_data = requests.get(api_link).json()

    with open(str(basedir) + "/request.json", "w", encoding='utf-8') as rq:
        json.dump(json_data, rq)


'''
    Read JSON file to show informations
'''
def read_json_file():
    with open(str(basedir) + "/request.json") as jf:
        data = json.load(jf)

    return data


'''
    Convert wind degrees to cardinal directions
'''
def degrees_to_cardinal(deg):
    dirs = ["NORD", "NNE", "NE", "ENE", 
            "EST", "ESE", "SE", "SSE", 
            "SUD", "SSO", "SO", "OSO", 
            "OUEST", "ONO", "NO", "NNO"]
    
    conversion = int((deg + 11.25)/22.5 - 0.02)
    return dirs[conversion % 16]



class MeteoOne(QMainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MeteoOne, self).__init__(*args, **kwargs)

        self.gui = Ui_MeteoOne()
        self.gui.setupUi(self)

        # -- First API request at start
        update_json_file()

        # ------------------------ Module descriptions ------------------------
        self.gui.time_desc_label.setText("HEURE ACTUELLE")
        self.gui.temp_desc_label.setText("TEMPERATURES")
        self.gui.feeling_desc_label.setText("RESSENTIE")
        self.gui.minimal_desc_label.setText("MINIMALE")
        self.gui.minimal_desc_label.setText("MINIMALE")
        self.gui.maximal_desc_label.setText("MAXIMALE")
        self.gui.wind_desc_label.setText("VENT")
        self.gui.pressure_desc_label.setText("PRESSION ATMOSPHERIQUE")
        self.gui.visibility_desc_label.setText("VISIBILITE")
        self.gui.humidity_desc_label.setText("HUMIDITE")
        self.gui.gps_desc_label.setText("COORDONNEES GPS")
        self.gui.gps_lat_desc_label.setText("LATITUDE")
        self.gui.gps_long_desc_label.setText("LONGITUDE")
        self.gui.sun_desc_button.setText("SOLEIL")
        self.gui.sunrise_desc_label.setText("SE LEVE A")
        self.gui.sunset_desc_label.setText("SE COUCHE A")

        '''
            Refresh widget every 0.5s
        '''
        self.widget_update = QTimer()
        self.widget_update.timeout.connect(self.show_widget)
        self.widget_update.start(500)

        self.loop = 0  # -- Initialise loop for request update --
        


    def show_widget(self):
        # -- Loop for JSON requests, every 10mn (1200)
        self.loop += 1
        if self.loop == 100:
            update_json_file()
            self.loop = 0

        '''
            Show TIME
        '''
        self.current_time = QTime.currentTime().toString('hh:mm')
        self.gui.time_label.setText(self.current_time)
        '''
            Show DATE
        '''
        self.current_date = datetime.now().strftime("%A %d %B %Y").upper()
        self.gui.date_label.setText(self.current_date)
        '''
            Show TEMPERATURES datas
        '''
        self.current_temp = int(read_json_file()['main']['temp'] - 273.15)
        self.gui.temp_label.setText(str(self.current_temp) + "°")

        self.feeling_temp = int(read_json_file()['main']['feels_like'] - 273.15)
        self.gui.feeling_temp_label.setText(str(self.feeling_temp) + "°")

        self.minimal_temp = int(read_json_file()['main']['temp_min'] - 273.15)
        self.gui.minimal_temp_label.setText(str(self.minimal_temp) + "°")

        self.maximal_temp = int(read_json_file()['main']['temp_max'] - 273.15)
        self.gui.maximal_temp_label.setText(str(self.maximal_temp) + "°")
        '''
            Show WIND datas
        '''
        # -- Show WIND speed --
        self.wind_speed_data = int(read_json_file()['wind']['speed'] * 3600 / 1000)
        self.gui.wind_speed_label.setText(str(self.wind_speed_data) + " KM/H")
        # -- Show WIND direction --
        self.wind_direction = read_json_file()['wind']['deg'] 
        self.gui.wind_orient_label.setText(degrees_to_cardinal(self.wind_direction))
        '''
            Show PRESSURE datas
        '''
        self.pressure_data = read_json_file()['main']['pressure']
        self.gui.pressure_info_label.setText(str(self.pressure_data) + " hPa")
        '''
            Show VISIBILITY datas
        '''
        self.visibiliy_data = int(read_json_file()['visibility'] / 1000)
        self.gui.visibiliy_info_label.setText(str(self.visibiliy_data) + " KM")
        '''
            Show HUMIDITY datas
        '''
        self.humidity_data = read_json_file()['main']['humidity']
        self.gui.humidity_info_label.setText(str(self.humidity_data) + " %")
        '''
            Show GPS datas
        '''
        # -- Show city name --
        self.city_name = read_json_file()['name']
        self.gui.city_name_label.setText(self.city_name.upper())
        # -- Show latitude coord --
        self.latitude_data = read_json_file()['coord']['lat']
        self.gui.latitude_label.setText(str(self.latitude_data))
        # -- Show longitude coord --
        self.longitude_data = read_json_file()['coord']['lon']
        self.gui.longitude_label.setText(str(self.longitude_data))
        '''
            Show SUN datas
        '''
        self.gui.sun_desc_button.clicked.connect(app.quit)
        # -- Show sunrise hour --
        self.sunrise_data = datetime.fromtimestamp(int(read_json_file()['sys']['sunrise']))
        self.sunrise_str = self.sunrise_data.strftime("%H:%M")
        self.gui.sunrise_label.setText(self.sunrise_str)
        # -- Show sunset hour --
        self.sunset_data = datetime.fromtimestamp(int(read_json_file()['sys']['sunset']))
        self.sunset_str = self.sunset_data.strftime("%H:%M")
        self.gui.sunset_label.setText(self.sunset_str)
    

        '''
            Switch between Day or Night
            Color RGB codes :
                Lime    = (0, 255, 0)
                Magenta = (255, 0, 255)
                Blue    = (0, 180, 255)
                Yellow  = (255, 255, 0)
        '''
        if "08:59" < self.current_time < "22:00":
            '''
                TIME color for light mode
            '''
            self.gui.time_desc_label.setStyleSheet("color: white; border: None")
            self.gui.time_label.setStyleSheet("color: rgb(0, 255, 0); border: None")
            '''
                DATE color for light mode
            '''
            self.gui.date_label.setStyleSheet("color: rgb(0, 180, 255); border: None")
            '''
                TEMPERATURE colors for light mode
            '''
            self.gui.temp_desc_label.setStyleSheet("color: white; border: None")
            # -- Current temperature --
            self.gui.temp_label.setStyleSheet("color: rgb(255, 140, 0); border: None")
            # -- Feels like --
            self.gui.feeling_desc_label.setStyleSheet("color: white; border: None")
            self.gui.feeling_temp_label.setStyleSheet("color: rgb(0, 255, 0); border: None")
            # -- Minimal --
            self.gui.minimal_desc_label.setStyleSheet("color: white; border: None")
            self.gui.minimal_temp_label.setStyleSheet("color: rgb(0, 180, 255); border: None")
            # -- Maximal --
            self.gui.maximal_desc_label.setStyleSheet("color: white; border: None")
            self.gui.maximal_temp_label.setStyleSheet("color: rgb(255, 0, 255); border: None")
            '''
                WIND color for light mode
            '''
            self.gui.wind_desc_label.setStyleSheet("color: white; border: None")
            # -- Speed --
            self.gui.wind_speed_label.setStyleSheet("color: rgb(0, 255, 0); border: None")
            # -- Direction --
            self.gui.wind_orient_label.setStyleSheet("color: rgb(0, 180, 255); border: None")
            '''
                PRESSURE color for light mode
            '''
            self.gui.pressure_desc_label.setStyleSheet("color: white; border: None")
            self.gui.pressure_info_label.setStyleSheet("color: rgb(255, 255, 0); border: None")
            '''
                VISIBILITY color for light mode
            '''
            self.gui.visibility_desc_label.setStyleSheet("color: white; border: None")
            self.gui.visibiliy_info_label.setStyleSheet("color: rgb(255, 0, 120); border: None")
            '''
                HUMIDITY color for light mode
            '''
            self.gui.humidity_desc_label.setStyleSheet("color: white; border: None")
            self.gui.humidity_info_label.setStyleSheet("color: rgb(0, 180, 255); border: None")
            '''
                GPS colors for light mode
            '''
            self.gui.gps_desc_label.setStyleSheet("color: white; border: None")
            # -- City name --
            self.gui.city_name_label.setStyleSheet("color: rgb(255, 255, 0); border: None")
            # -- Latitude --
            self.gui.gps_lat_desc_label.setStyleSheet("color: white; border: None")
            self.gui.latitude_label.setStyleSheet("color: rgb(200, 0, 255); border: None")
            # -- Longitude --
            self.gui.gps_long_desc_label.setStyleSheet("color: white; border: None")
            self.gui.longitude_label.setStyleSheet("color: rgb(0, 255, 100); border: None")
            '''
                SUN colors for light mode
            '''
            self.gui.sun_desc_button.setStyleSheet("color: white; border: None")
            # -- Sunrise hour --
            self.gui.sunrise_desc_label.setStyleSheet("color: white; border: None")
            self.gui.sunrise_label.setStyleSheet("color: rgb(255, 180, 0); border: None")
            # -- Sunset hour --
            self.gui.sunset_desc_label.setStyleSheet("color: white; border: None")
            self.gui.sunset_label.setStyleSheet("color: rgb(255, 0, 120); border: None")

            '''
                IMAGES selection for light mode
            '''
            if read_json_file()['weather'][0]['description'] == "ciel dégagé":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/sun.png'))
            
            if read_json_file()['weather'][0]['description'] == "peu nuageux":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/few_cloudy_sun.png'))

            if read_json_file()['weather'][0]['description'] == "partiellement nuageux":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/cloudy_sun.png'))

            if read_json_file()['weather'][0]['description'] == "couvert" or \
            read_json_file()['weather'][0]['description'] == "nuageux":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/cloudy_day.png'))

            if read_json_file()['weather'][0]['description'] == "légère pluie" or \
            read_json_file()['weather'][0]['description'] == "pluie modérée":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/light_rain_day.png'))

            if read_json_file()['weather'][0]['description'] == "orage":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/storm_day.png'))

            if read_json_file()['weather'][0]['description'] == "brume" or \
            read_json_file()['weather'][0]['description'] == "brouillard":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/mist_day.png'))

            if read_json_file()['weather'][0]['description'] == "forte pluie":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/rain_day.png'))

        else:
            '''
                TIME color for dark mode
            '''
            self.gui.time_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.time_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                DATE color for dark mode
            '''
            self.gui.date_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                TEMPERATURE color for dark mode
            '''
            self.gui.temp_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Current temperature --
            self.gui.temp_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Feels like --
            self.gui.feeling_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.feeling_temp_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Minimal --
            self.gui.minimal_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.minimal_temp_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Maximal --
            self.gui.maximal_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.maximal_temp_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                WIND color for dark mode
            '''
            self.gui.wind_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Speed --
            self.gui.wind_speed_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Direction --
            self.gui.wind_orient_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                PRESSURE color for dark mode
            '''
            self.gui.pressure_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.pressure_info_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                VISIBILITY color for dark mode
            '''
            self.gui.visibility_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.visibiliy_info_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                HUMIDITY color for dark mode
            '''
            self.gui.humidity_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.humidity_info_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                GPS color for dark mode
            '''
            self.gui.gps_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- City name --
            self.gui.city_name_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Latitude --
            self.gui.gps_lat_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.latitude_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Longitude --
            self.gui.gps_long_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.longitude_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            '''
                SUN color for dark mode
            '''
            self.gui.sun_desc_button.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Sunrise hour --
            self.gui.sunrise_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.sunrise_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            # -- Sunset hour --
            self.gui.sunset_desc_label.setStyleSheet("color: rgb(35, 35, 35); border: None")
            self.gui.sunset_label.setStyleSheet("color: rgb(35, 35, 35); border: None")

            '''
                IMAGES selection for dark mode
            '''
            if read_json_file()['weather'][0]['description'] == "ciel dégagé":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/moon.png'))

            if read_json_file()['weather'][0]['description'] == "peu nuageux":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/few_cloudy_moon.png'))

            if read_json_file()['weather'][0]['description'] == "partiellement nuageux":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/cloudy_moon.png'))

            if read_json_file()['weather'][0]['description'] == "couvert" or \
            read_json_file()['weather'][0]['description'] == "nuageux":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/cloudy_night.png'))

            if read_json_file()['weather'][0]['description'] == "légère pluie" or \
            read_json_file()['weather'][0]['description'] == "pluie modérée":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/light_rain_night.png'))

            if read_json_file()['weather'][0]['description'] == "orage":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/storm_night.png'))

            if read_json_file()['weather'][0]['description'] == "brume" or \
            read_json_file()['weather'][0]['description'] == "brouillard":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/mist_night.png'))

            if read_json_file()['weather'][0]['description'] == "forte pluie":
                self.gui.image_label.setStyleSheet("border: None")
                self.gui.image_label.setPixmap(QPixmap(str(basedir) + '/pics/rain_night.png'))




import sys

app = QApplication(sys.argv)

widget = MeteoOne()
# -- Hide mouse cursor --
widget.setCursor(Qt.CursorShape.BlankCursor)
# -- Hide title bar --
widget.setWindowFlags(Qt.WindowType.FramelessWindowHint)
# -- Full screen mode --
#widget.showFullScreen()
# -- Windowed screen mode --
widget.show()

app.exec()