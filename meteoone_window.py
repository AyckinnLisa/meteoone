# Form implementation generated from reading ui file 'meteoone_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MeteoOne(object):
    def setupUi(self, MeteoOne):
        MeteoOne.setObjectName("MeteoOne")
        MeteoOne.resize(1024, 600)
        MeteoOne.setMinimumSize(QtCore.QSize(1024, 600))
        MeteoOne.setMaximumSize(QtCore.QSize(1024, 600))
        MeteoOne.setStyleSheet("background-color: rgb(0, 10, 20);")
        self.date_frame = QtWidgets.QFrame(parent=MeteoOne)
        self.date_frame.setGeometry(QtCore.QRect(10, 240, 1001, 61))
        self.date_frame.setStyleSheet("border: 2px solid rgb(30,30,30);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.date_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.date_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.date_frame.setLineWidth(5)
        self.date_frame.setObjectName("date_frame")
        self.date_label = QtWidgets.QLabel(parent=self.date_frame)
        self.date_label.setGeometry(QtCore.QRect(17, 6, 971, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("border: None;")
        self.date_label.setLineWidth(0)
        self.date_label.setText("")
        self.date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.time_frame = QtWidgets.QFrame(parent=MeteoOne)
        self.time_frame.setGeometry(QtCore.QRect(360, 310, 301, 161))
        self.time_frame.setStyleSheet("border: 2px solid rgb(25,25,25);")
        self.time_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.time_frame.setLineWidth(5)
        self.time_frame.setObjectName("time_frame")
        self.time_label = QtWidgets.QLabel(parent=self.time_frame)
        self.time_label.setGeometry(QtCore.QRect(10, 30, 281, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(80)
        font.setBold(True)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("border: None;")
        self.time_label.setText("")
        self.time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.time_desc_label = QtWidgets.QLabel(parent=self.time_frame)
        self.time_desc_label.setGeometry(QtCore.QRect(10, 20, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.time_desc_label.setFont(font)
        self.time_desc_label.setStyleSheet("border: None;")
        self.time_desc_label.setText("")
        self.time_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_desc_label.setObjectName("time_desc_label")
        self.layoutWidget = QtWidgets.QWidget(parent=MeteoOne)
        self.layoutWidget.setGeometry(QtCore.QRect(670, 310, 341, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.presvis_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.presvis_layout.setContentsMargins(0, 0, 0, 0)
        self.presvis_layout.setObjectName("presvis_layout")
        self.pressure_frame = QtWidgets.QFrame(parent=self.layoutWidget)
        self.pressure_frame.setStyleSheet("border: 2px solid rgb(25,25,25);")
        self.pressure_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.pressure_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pressure_frame.setLineWidth(5)
        self.pressure_frame.setObjectName("pressure_frame")
        self.pressure_desc_label = QtWidgets.QLabel(parent=self.pressure_frame)
        self.pressure_desc_label.setGeometry(QtCore.QRect(10, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.pressure_desc_label.setFont(font)
        self.pressure_desc_label.setStyleSheet("border: None;")
        self.pressure_desc_label.setText("")
        self.pressure_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pressure_desc_label.setObjectName("pressure_desc_label")
        self.pressure_info_label = QtWidgets.QLabel(parent=self.pressure_frame)
        self.pressure_info_label.setGeometry(QtCore.QRect(18, 40, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.pressure_info_label.setFont(font)
        self.pressure_info_label.setStyleSheet("border: None;")
        self.pressure_info_label.setText("")
        self.pressure_info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pressure_info_label.setObjectName("pressure_info_label")
        self.presvis_layout.addWidget(self.pressure_frame)
        self.visibility_frame = QtWidgets.QFrame(parent=self.layoutWidget)
        self.visibility_frame.setStyleSheet("border: 2px solid rgb(25,25,25);")
        self.visibility_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.visibility_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.visibility_frame.setLineWidth(5)
        self.visibility_frame.setObjectName("visibility_frame")
        self.visibility_desc_label = QtWidgets.QLabel(parent=self.visibility_frame)
        self.visibility_desc_label.setGeometry(QtCore.QRect(10, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.visibility_desc_label.setFont(font)
        self.visibility_desc_label.setStyleSheet("border: None;")
        self.visibility_desc_label.setText("")
        self.visibility_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.visibility_desc_label.setObjectName("visibility_desc_label")
        self.visibiliy_info_label = QtWidgets.QLabel(parent=self.visibility_frame)
        self.visibiliy_info_label.setGeometry(QtCore.QRect(10, 40, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.visibiliy_info_label.setFont(font)
        self.visibiliy_info_label.setStyleSheet("border: None;")
        self.visibiliy_info_label.setText("")
        self.visibiliy_info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.visibiliy_info_label.setObjectName("visibiliy_info_label")
        self.presvis_layout.addWidget(self.visibility_frame)
        self.layoutWidget1 = QtWidgets.QWidget(parent=MeteoOne)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 1001, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gps_frame = QtWidgets.QFrame(parent=self.layoutWidget1)
        self.gps_frame.setStyleSheet("border: 2px solid rgb(25,25,25);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gps_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.gps_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gps_frame.setLineWidth(5)
        self.gps_frame.setObjectName("gps_frame")
        self.gps_desc_label = QtWidgets.QLabel(parent=self.gps_frame)
        self.gps_desc_label.setGeometry(QtCore.QRect(10, 10, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.gps_desc_label.setFont(font)
        self.gps_desc_label.setStyleSheet("border: None;")
        self.gps_desc_label.setText("")
        self.gps_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gps_desc_label.setObjectName("gps_desc_label")
        self.city_name_label = QtWidgets.QLabel(parent=self.gps_frame)
        self.city_name_label.setGeometry(QtCore.QRect(10, 60, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        self.city_name_label.setFont(font)
        self.city_name_label.setStyleSheet("border: None;")
        self.city_name_label.setText("")
        self.city_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.city_name_label.setObjectName("city_name_label")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.gps_frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 111, 281, 20))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.longlat_desc_layout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.longlat_desc_layout.setContentsMargins(0, 0, 0, 0)
        self.longlat_desc_layout.setSpacing(0)
        self.longlat_desc_layout.setObjectName("longlat_desc_layout")
        self.gps_lat_desc_label = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.gps_lat_desc_label.setFont(font)
        self.gps_lat_desc_label.setStyleSheet("border: None;")
        self.gps_lat_desc_label.setText("")
        self.gps_lat_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gps_lat_desc_label.setObjectName("gps_lat_desc_label")
        self.longlat_desc_layout.addWidget(self.gps_lat_desc_label)
        self.gps_long_desc_label = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.gps_long_desc_label.setFont(font)
        self.gps_long_desc_label.setStyleSheet("border: None;")
        self.gps_long_desc_label.setText("")
        self.gps_long_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gps_long_desc_label.setObjectName("gps_long_desc_label")
        self.longlat_desc_layout.addWidget(self.gps_long_desc_label)
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.gps_frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 140, 281, 34))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.longlat_layout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.longlat_layout.setContentsMargins(0, 0, 0, 0)
        self.longlat_layout.setSpacing(0)
        self.longlat_layout.setObjectName("longlat_layout")
        self.latitude_label = QtWidgets.QLabel(parent=self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        self.latitude_label.setFont(font)
        self.latitude_label.setStyleSheet("border: None;")
        self.latitude_label.setText("")
        self.latitude_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.latitude_label.setObjectName("latitude_label")
        self.longlat_layout.addWidget(self.latitude_label)
        self.longitude_label = QtWidgets.QLabel(parent=self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        self.longitude_label.setFont(font)
        self.longitude_label.setStyleSheet("border: None;")
        self.longitude_label.setText("")
        self.longitude_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.longitude_label.setObjectName("longitude_label")
        self.longlat_layout.addWidget(self.longitude_label)
        self.horizontalLayout.addWidget(self.gps_frame)
        self.conditions_frame = QtWidgets.QFrame(parent=self.layoutWidget1)
        self.conditions_frame.setStyleSheet("border: 2px solid rgb(25,25,25);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.conditions_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.conditions_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.conditions_frame.setLineWidth(5)
        self.conditions_frame.setObjectName("conditions_frame")
        self.image_label = QtWidgets.QLabel(parent=self.conditions_frame)
        self.image_label.setGeometry(QtCore.QRect(21, 8, 281, 201))
        self.image_label.setStyleSheet("border: None")
        self.image_label.setText("")
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.conditions_frame)
        self.temp_frame = QtWidgets.QFrame(parent=self.layoutWidget1)
        self.temp_frame.setStyleSheet("border: 2px solid rgb(25,25,25);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.temp_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.temp_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.temp_frame.setLineWidth(5)
        self.temp_frame.setObjectName("temp_frame")
        self.temp_desc_label = QtWidgets.QLabel(parent=self.temp_frame)
        self.temp_desc_label.setGeometry(QtCore.QRect(10, 11, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.temp_desc_label.setFont(font)
        self.temp_desc_label.setStyleSheet("border: None;")
        self.temp_desc_label.setText("")
        self.temp_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.temp_desc_label.setObjectName("temp_desc_label")
        self.temp_label = QtWidgets.QLabel(parent=self.temp_frame)
        self.temp_label.setGeometry(QtCore.QRect(10, 50, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(85)
        font.setBold(True)
        self.temp_label.setFont(font)
        self.temp_label.setStyleSheet("border: None;")
        self.temp_label.setText("")
        self.temp_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setObjectName("temp_label")
        self.layoutWidget4 = QtWidgets.QWidget(parent=self.temp_frame)
        self.layoutWidget4.setGeometry(QtCore.QRect(6, 145, 311, 31))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.temp_desc_layout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.temp_desc_layout.setContentsMargins(0, 0, 0, 0)
        self.temp_desc_layout.setSpacing(0)
        self.temp_desc_layout.setObjectName("temp_desc_layout")
        self.feeling_desc_label = QtWidgets.QLabel(parent=self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.feeling_desc_label.setFont(font)
        self.feeling_desc_label.setStyleSheet("border: None;")
        self.feeling_desc_label.setText("")
        self.feeling_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.feeling_desc_label.setObjectName("feeling_desc_label")
        self.temp_desc_layout.addWidget(self.feeling_desc_label)
        self.minimal_desc_label = QtWidgets.QLabel(parent=self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.minimal_desc_label.setFont(font)
        self.minimal_desc_label.setStyleSheet("border: None;")
        self.minimal_desc_label.setText("")
        self.minimal_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.minimal_desc_label.setObjectName("minimal_desc_label")
        self.temp_desc_layout.addWidget(self.minimal_desc_label)
        self.maximal_desc_label = QtWidgets.QLabel(parent=self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.maximal_desc_label.setFont(font)
        self.maximal_desc_label.setStyleSheet("border: None;")
        self.maximal_desc_label.setText("")
        self.maximal_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.maximal_desc_label.setObjectName("maximal_desc_label")
        self.temp_desc_layout.addWidget(self.maximal_desc_label)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.temp_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(6, 170, 311, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.temp_layout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.temp_layout.setContentsMargins(0, 0, 0, 0)
        self.temp_layout.setSpacing(0)
        self.temp_layout.setObjectName("temp_layout")
        self.feeling_temp_label = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.feeling_temp_label.setFont(font)
        self.feeling_temp_label.setStyleSheet("border: None;")
        self.feeling_temp_label.setText("")
        self.feeling_temp_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.feeling_temp_label.setObjectName("feeling_temp_label")
        self.temp_layout.addWidget(self.feeling_temp_label)
        self.minimal_temp_label = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.minimal_temp_label.setFont(font)
        self.minimal_temp_label.setStyleSheet("border: None;")
        self.minimal_temp_label.setText("")
        self.minimal_temp_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.minimal_temp_label.setObjectName("minimal_temp_label")
        self.temp_layout.addWidget(self.minimal_temp_label)
        self.maximal_temp_label = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.maximal_temp_label.setFont(font)
        self.maximal_temp_label.setStyleSheet("border: None;")
        self.maximal_temp_label.setText("")
        self.maximal_temp_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.maximal_temp_label.setObjectName("maximal_temp_label")
        self.temp_layout.addWidget(self.maximal_temp_label)
        self.horizontalLayout.addWidget(self.temp_frame)
        self.layoutWidget5 = QtWidgets.QWidget(parent=MeteoOne)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 310, 341, 281))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.sun_wind_layout = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.sun_wind_layout.setContentsMargins(0, 0, 0, 0)
        self.sun_wind_layout.setObjectName("sun_wind_layout")
        self.wind_frame = QtWidgets.QFrame(parent=self.layoutWidget5)
        self.wind_frame.setStyleSheet("border: 2px solid rgb(25,25,25);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.wind_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.wind_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.wind_frame.setLineWidth(5)
        self.wind_frame.setObjectName("wind_frame")
        self.wind_desc_label = QtWidgets.QLabel(parent=self.wind_frame)
        self.wind_desc_label.setGeometry(QtCore.QRect(10, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.wind_desc_label.setFont(font)
        self.wind_desc_label.setStyleSheet("border: None;")
        self.wind_desc_label.setText("")
        self.wind_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wind_desc_label.setObjectName("wind_desc_label")
        self.layoutWidget6 = QtWidgets.QWidget(parent=self.wind_frame)
        self.layoutWidget6.setGeometry(QtCore.QRect(30, 43, 301, 71))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.wind_layout = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.wind_layout.setContentsMargins(0, 0, 0, 0)
        self.wind_layout.setSpacing(0)
        self.wind_layout.setObjectName("wind_layout")
        self.wind_speed_label = QtWidgets.QLabel(parent=self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.wind_speed_label.setFont(font)
        self.wind_speed_label.setStyleSheet("border: None;")
        self.wind_speed_label.setText("")
        self.wind_speed_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wind_speed_label.setObjectName("wind_speed_label")
        self.wind_layout.addWidget(self.wind_speed_label)
        self.wind_orient_label = QtWidgets.QLabel(parent=self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.wind_orient_label.setFont(font)
        self.wind_orient_label.setStyleSheet("border: None;")
        self.wind_orient_label.setText("")
        self.wind_orient_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wind_orient_label.setObjectName("wind_orient_label")
        self.wind_layout.addWidget(self.wind_orient_label)
        self.sun_wind_layout.addWidget(self.wind_frame)
        self.sun_frame = QtWidgets.QFrame(parent=self.layoutWidget5)
        self.sun_frame.setStyleSheet("border: 2px solid rgb(25,25,25);")
        self.sun_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.sun_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sun_frame.setLineWidth(5)
        self.sun_frame.setObjectName("sun_frame")
        self.layoutWidget7 = QtWidgets.QWidget(parent=self.sun_frame)
        self.layoutWidget7.setGeometry(QtCore.QRect(20, 40, 301, 21))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.sunrisesunset_desc_layout = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.sunrisesunset_desc_layout.setContentsMargins(0, 0, 0, 0)
        self.sunrisesunset_desc_layout.setSpacing(0)
        self.sunrisesunset_desc_layout.setObjectName("sunrisesunset_desc_layout")
        self.sunrise_desc_label = QtWidgets.QLabel(parent=self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.sunrise_desc_label.setFont(font)
        self.sunrise_desc_label.setStyleSheet("border: None;")
        self.sunrise_desc_label.setText("")
        self.sunrise_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sunrise_desc_label.setObjectName("sunrise_desc_label")
        self.sunrisesunset_desc_layout.addWidget(self.sunrise_desc_label)
        self.sunset_desc_label = QtWidgets.QLabel(parent=self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.sunset_desc_label.setFont(font)
        self.sunset_desc_label.setStyleSheet("border: None;")
        self.sunset_desc_label.setText("")
        self.sunset_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sunset_desc_label.setObjectName("sunset_desc_label")
        self.sunrisesunset_desc_layout.addWidget(self.sunset_desc_label)
        self.layoutWidget8 = QtWidgets.QWidget(parent=self.sun_frame)
        self.layoutWidget8.setGeometry(QtCore.QRect(20, 70, 301, 51))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.sunrisesunset_layout = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.sunrisesunset_layout.setContentsMargins(0, 0, 0, 0)
        self.sunrisesunset_layout.setSpacing(0)
        self.sunrisesunset_layout.setObjectName("sunrisesunset_layout")
        self.sunrise_label = QtWidgets.QLabel(parent=self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.sunrise_label.setFont(font)
        self.sunrise_label.setStyleSheet("border: None;")
        self.sunrise_label.setText("")
        self.sunrise_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sunrise_label.setObjectName("sunrise_label")
        self.sunrisesunset_layout.addWidget(self.sunrise_label)
        self.sunset_label = QtWidgets.QLabel(parent=self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.sunset_label.setFont(font)
        self.sunset_label.setStyleSheet("border: None;")
        self.sunset_label.setText("")
        self.sunset_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sunset_label.setObjectName("sunset_label")
        self.sunrisesunset_layout.addWidget(self.sunset_label)
        self.sun_desc_button = QtWidgets.QPushButton(parent=self.sun_frame)
        self.sun_desc_button.setGeometry(QtCore.QRect(10, 5, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sun_desc_button.setFont(font)
        self.sun_desc_button.setStyleSheet("border: None")
        self.sun_desc_button.setText("")
        self.sun_desc_button.setObjectName("sun_desc_button")
        self.sun_wind_layout.addWidget(self.sun_frame)
        self.humidity_frame = QtWidgets.QFrame(parent=MeteoOne)
        self.humidity_frame.setGeometry(QtCore.QRect(360, 480, 301, 111))
        self.humidity_frame.setStyleSheet("border: 2px solid rgb(25,25,25);")
        self.humidity_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.humidity_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.humidity_frame.setLineWidth(5)
        self.humidity_frame.setObjectName("humidity_frame")
        self.humidity_desc_label = QtWidgets.QLabel(parent=self.humidity_frame)
        self.humidity_desc_label.setGeometry(QtCore.QRect(10, 10, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.humidity_desc_label.setFont(font)
        self.humidity_desc_label.setStyleSheet("border: None;")
        self.humidity_desc_label.setText("")
        self.humidity_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.humidity_desc_label.setObjectName("humidity_desc_label")
        self.humidity_info_label = QtWidgets.QLabel(parent=self.humidity_frame)
        self.humidity_info_label.setGeometry(QtCore.QRect(10, 30, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        self.humidity_info_label.setFont(font)
        self.humidity_info_label.setStyleSheet("border: None;")
        self.humidity_info_label.setText("")
        self.humidity_info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.humidity_info_label.setObjectName("humidity_info_label")

        self.retranslateUi(MeteoOne)
        QtCore.QMetaObject.connectSlotsByName(MeteoOne)

    def retranslateUi(self, MeteoOne):
        _translate = QtCore.QCoreApplication.translate
        MeteoOne.setWindowTitle(_translate("MeteoOne", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MeteoOne = QtWidgets.QWidget()
    ui = Ui_MeteoOne()
    ui.setupUi(MeteoOne)
    MeteoOne.show()
    sys.exit(app.exec())