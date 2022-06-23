# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import pvcd_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 733)
        MainWindow.setMaximumSize(QSize(16777215, 733))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(60,63,65);")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sidenav = QFrame(self.centralwidget)
        self.sidenav.setObjectName(u"sidenav")
        self.sidenav.setFrameShape(QFrame.StyledPanel)
        self.sidenav.setFrameShadow(QFrame.Raised)
        self.sidenav.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.sidenav)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.sidenav)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.menu.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.menu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menu_top = QFrame(self.menu)
        self.menu_top.setObjectName(u"menu_top")
        self.menu_top.setMaximumSize(QSize(16777215, 150))
        self.menu_top.setFrameShape(QFrame.StyledPanel)
        self.menu_top.setFrameShadow(QFrame.Raised)
        self.menu_top.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.menu_top)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidenav_title_label = QLabel(self.menu_top)
        self.sidenav_title_label.setObjectName(u"sidenav_title_label")
        self.sidenav_title_label.setMinimumSize(QSize(0, 30))
        self.sidenav_title_label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.sidenav_title_label.setFont(font)
        self.sidenav_title_label.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.sidenav_title_label)

        self.page_1_btn = QPushButton(self.menu_top)
        self.page_1_btn.setObjectName(u"page_1_btn")
        self.page_1_btn.setMinimumSize(QSize(60, 60))
        self.page_1_btn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,82,84);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(45,47,48);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/16x16/resource/icons/16x16/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_1_btn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.page_1_btn)

        self.page_2_btn = QPushButton(self.menu_top)
        self.page_2_btn.setObjectName(u"page_2_btn")
        self.page_2_btn.setMinimumSize(QSize(60, 60))
        self.page_2_btn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,82,84);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(45,47,48);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/16x16/resource/icons/16x16/cil-paint-bucket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_2_btn.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.page_2_btn)


        self.verticalLayout_8.addWidget(self.menu_top)

        self.menu_bottom = QFrame(self.menu)
        self.menu_bottom.setObjectName(u"menu_bottom")
        self.menu_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.menu_bottom.setFrameShape(QFrame.StyledPanel)
        self.menu_bottom.setFrameShadow(QFrame.Raised)
        self.menu_bottom.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.menu_bottom)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.menu_bottom)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.btn_setting = QPushButton(self.menu_bottom)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(60, 60))
        self.btn_setting.setMaximumSize(QSize(16777215, 60))
        self.btn_setting.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,82,84);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(45,47,48);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/16x16/resource/icons/16x16/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon2)

        self.verticalLayout.addWidget(self.btn_setting)


        self.verticalLayout_8.addWidget(self.menu_bottom)


        self.verticalLayout_3.addWidget(self.menu)


        self.horizontalLayout_3.addWidget(self.sidenav)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.window = QFrame(self.frame_2)
        self.window.setObjectName(u"window")
        self.window.setMaximumSize(QSize(16777215, 50))
        self.window.setFrameShape(QFrame.StyledPanel)
        self.window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.window)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.win_title_label = QLabel(self.window)
        self.win_title_label.setObjectName(u"win_title_label")
        self.win_title_label.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.win_title_label.setFont(font1)
        self.win_title_label.setStyleSheet(u"color: rgb(159,160,161);")

        self.horizontalLayout.addWidget(self.win_title_label)

        self.window_btns = QFrame(self.window)
        self.window_btns.setObjectName(u"window_btns")
        self.window_btns.setMaximumSize(QSize(120, 16777215))
        self.window_btns.setFrameShape(QFrame.StyledPanel)
        self.window_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.window_btns)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.win_minimize_btn = QPushButton(self.window_btns)
        self.win_minimize_btn.setObjectName(u"win_minimize_btn")
        self.win_minimize_btn.setMinimumSize(QSize(0, 30))
        self.win_minimize_btn.setMaximumSize(QSize(40, 16777215))
        self.win_minimize_btn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,82,84);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(45,47,48);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/16x16/resource/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.win_minimize_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.win_minimize_btn)

        self.win_maximize_btn = QPushButton(self.window_btns)
        self.win_maximize_btn.setObjectName(u"win_maximize_btn")
        self.win_maximize_btn.setMinimumSize(QSize(0, 30))
        self.win_maximize_btn.setMaximumSize(QSize(40, 16777215))
        self.win_maximize_btn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,82,84);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(45,47,48);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/16x16/resource/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.win_maximize_btn.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.win_maximize_btn)

        self.win_close_btn = QPushButton(self.window_btns)
        self.win_close_btn.setObjectName(u"win_close_btn")
        self.win_close_btn.setMinimumSize(QSize(0, 30))
        self.win_close_btn.setMaximumSize(QSize(40, 16777215))
        self.win_close_btn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,82,84);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(45,47,48);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/16x16/resource/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.win_close_btn.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.win_close_btn)


        self.horizontalLayout.addWidget(self.window_btns)


        self.verticalLayout_6.addWidget(self.window)

        self.content = QFrame(self.frame_2)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.content.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.page_header = QLabel(self.content)
        self.page_header.setObjectName(u"page_header")
        self.page_header.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.page_header.setFont(font2)
        self.page_header.setStyleSheet(u"color: rgb(130, 130, 130);\n"
"background-color: rgb(80,80,80);")
        self.page_header.setLineWidth(0)
        self.page_header.setMargin(0)
        self.page_header.setIndent(10)

        self.verticalLayout_4.addWidget(self.page_header)

        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(43,43,43);")
        self.stackedWidget.setLineWidth(0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.page_1)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.query = QWidget(self.widget_2)
        self.query.setObjectName(u"query")
        self.query.setMaximumSize(QSize(550, 16777215))
        font3 = QFont()
        font3.setFamilies([u"\ub9d1\uc740 \uace0\ub515 Semilight"])
        self.query.setFont(font3)
        self.query.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.query)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 0, 0, 0)
        self.viewer = QFrame(self.query)
        self.viewer.setObjectName(u"viewer")
        self.viewer.setMaximumSize(QSize(16777215, 16777215))
        self.viewer.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(49,50,51);\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton { \n"
"	background-color: rgb(149,150,151);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPushButton:disabled{\n"
"	border: 2px solid rgb(80, 80, 80);\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.viewer.setFrameShape(QFrame.StyledPanel)
        self.viewer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.viewer)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(30, 10, 30, 10)
        self.label = QLabel(self.viewer)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.label.setFont(font4)

        self.verticalLayout_22.addWidget(self.label)

        self.frame_12 = QFrame(self.viewer)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setMaximumSize(QSize(16777215, 30))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.query_open_le = QLineEdit(self.frame_12)
        self.query_open_le.setObjectName(u"query_open_le")
        self.query_open_le.setMinimumSize(QSize(0, 30))
        self.query_open_le.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        self.query_open_le.setFont(font5)
        self.query_open_le.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.query_open_le)

        self.query_open_btn = QPushButton(self.frame_12)
        self.query_open_btn.setObjectName(u"query_open_btn")
        self.query_open_btn.setMinimumSize(QSize(80, 30))
        self.query_open_btn.setMaximumSize(QSize(80, 30))
        self.query_open_btn.setFont(font2)

        self.horizontalLayout_15.addWidget(self.query_open_btn)


        self.verticalLayout_22.addWidget(self.frame_12)

        self.frame_30 = QFrame(self.viewer)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(320, 240))
        self.frame_30.setMaximumSize(QSize(16777215, 360))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.query_image = QLabel(self.frame_30)
        self.query_image.setObjectName(u"query_image")
        self.query_image.setMinimumSize(QSize(480, 360))
        self.query_image.setMaximumSize(QSize(480, 360))
        self.query_image.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.query_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.query_image)


        self.verticalLayout_22.addWidget(self.frame_30)


        self.verticalLayout_10.addWidget(self.viewer)

        self.query_controls = QFrame(self.query)
        self.query_controls.setObjectName(u"query_controls")
        self.query_controls.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(49,50,51);\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton { \n"
"	background-color: rgb(149,150,151);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPushButton:disabled{\n"
"	border: 2px solid rgb(43,43,43);\n"
"	background-color: rgb(43,43,43);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.query_controls.setFrameShape(QFrame.StyledPanel)
        self.query_controls.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.query_controls)
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(30, 20, 30, 10)
        self.frame_34 = QFrame(self.query_controls)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_34)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_34)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(120, 30))
        self.label_6.setMaximumSize(QSize(120, 30))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_6)

        self.label_5 = QLabel(self.frame_34)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 30))
        self.label_5.setMaximumSize(QSize(120, 30))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_5)

        self.label_8 = QLabel(self.frame_34)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 30))
        self.label_8.setMaximumSize(QSize(120, 30))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_8)

        self.label_3 = QLabel(self.frame_34)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 30))
        self.label_3.setMaximumSize(QSize(120, 30))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_3)

        self.frame_31 = QFrame(self.frame_34)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_31)


        self.horizontalLayout_32.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.query_controls)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"}\n"
"QLabel:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_33)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.query_topk_label = QLabel(self.frame_33)
        self.query_topk_label.setObjectName(u"query_topk_label")
        self.query_topk_label.setMinimumSize(QSize(80, 30))
        self.query_topk_label.setMaximumSize(QSize(80, 30))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        self.query_topk_label.setFont(font6)
        self.query_topk_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.query_topk_label)

        self.query_wnd_label = QLabel(self.frame_33)
        self.query_wnd_label.setObjectName(u"query_wnd_label")
        self.query_wnd_label.setMinimumSize(QSize(80, 30))
        self.query_wnd_label.setMaximumSize(QSize(80, 30))
        self.query_wnd_label.setFont(font6)
        self.query_wnd_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.query_wnd_label)

        self.query_score_thr_label = QLabel(self.frame_33)
        self.query_score_thr_label.setObjectName(u"query_score_thr_label")
        self.query_score_thr_label.setMinimumSize(QSize(80, 30))
        self.query_score_thr_label.setMaximumSize(QSize(80, 30))
        self.query_score_thr_label.setFont(font6)
        self.query_score_thr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.query_score_thr_label)

        self.query_match_thr_label = QLabel(self.frame_33)
        self.query_match_thr_label.setObjectName(u"query_match_thr_label")
        self.query_match_thr_label.setMinimumSize(QSize(80, 30))
        self.query_match_thr_label.setMaximumSize(QSize(80, 30))
        self.query_match_thr_label.setFont(font6)
        self.query_match_thr_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.query_match_thr_label)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_35)


        self.horizontalLayout_32.addWidget(self.frame_33)

        self.frame_32 = QFrame(self.query_controls)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"QSlider{\n"
"	background:transparent;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"	border-color: rgba(80,80,80,150);\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgba(80,80,80,150);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(46,46,51);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_32)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, 0, 0, 0)
        self.query_topk_slider = QSlider(self.frame_32)
        self.query_topk_slider.setObjectName(u"query_topk_slider")
        self.query_topk_slider.setMinimumSize(QSize(0, 30))
        self.query_topk_slider.setMinimum(1)
        self.query_topk_slider.setMaximum(10)
        self.query_topk_slider.setPageStep(1)
        self.query_topk_slider.setValue(2)
        self.query_topk_slider.setOrientation(Qt.Horizontal)
        self.query_topk_slider.setTickInterval(50)

        self.verticalLayout_24.addWidget(self.query_topk_slider)

        self.query_wnd_slider = QSlider(self.frame_32)
        self.query_wnd_slider.setObjectName(u"query_wnd_slider")
        self.query_wnd_slider.setMinimumSize(QSize(0, 30))
        self.query_wnd_slider.setMinimum(2)
        self.query_wnd_slider.setMaximum(20)
        self.query_wnd_slider.setPageStep(1)
        self.query_wnd_slider.setValue(10)
        self.query_wnd_slider.setOrientation(Qt.Horizontal)
        self.query_wnd_slider.setTickInterval(1)

        self.verticalLayout_24.addWidget(self.query_wnd_slider)

        self.query_score_thr_slider = QSlider(self.frame_32)
        self.query_score_thr_slider.setObjectName(u"query_score_thr_slider")
        self.query_score_thr_slider.setMinimumSize(QSize(0, 30))
        self.query_score_thr_slider.setMinimum(2)
        self.query_score_thr_slider.setMaximum(20)
        self.query_score_thr_slider.setPageStep(1)
        self.query_score_thr_slider.setValue(12)
        self.query_score_thr_slider.setOrientation(Qt.Horizontal)
        self.query_score_thr_slider.setTickInterval(5)

        self.verticalLayout_24.addWidget(self.query_score_thr_slider)

        self.query_match_thr_slider = QSlider(self.frame_32)
        self.query_match_thr_slider.setObjectName(u"query_match_thr_slider")
        self.query_match_thr_slider.setMinimumSize(QSize(0, 30))
        self.query_match_thr_slider.setMinimum(2)
        self.query_match_thr_slider.setMaximum(20)
        self.query_match_thr_slider.setPageStep(1)
        self.query_match_thr_slider.setValue(3)
        self.query_match_thr_slider.setOrientation(Qt.Horizontal)
        self.query_match_thr_slider.setTickInterval(1)

        self.verticalLayout_24.addWidget(self.query_match_thr_slider)

        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_33.setSpacing(5)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.query_reset_btn = QPushButton(self.frame_36)
        self.query_reset_btn.setObjectName(u"query_reset_btn")
        self.query_reset_btn.setMinimumSize(QSize(0, 30))
        self.query_reset_btn.setFont(font)

        self.horizontalLayout_33.addWidget(self.query_reset_btn)

        self.query_submit_btn = QPushButton(self.frame_36)
        self.query_submit_btn.setObjectName(u"query_submit_btn")
        self.query_submit_btn.setMinimumSize(QSize(0, 30))
        self.query_submit_btn.setFont(font)

        self.horizontalLayout_33.addWidget(self.query_submit_btn)


        self.verticalLayout_24.addWidget(self.frame_36)


        self.horizontalLayout_32.addWidget(self.frame_32)


        self.verticalLayout_10.addWidget(self.query_controls)


        self.horizontalLayout_7.addWidget(self.query)

        self.result = QFrame(self.widget_2)
        self.result.setObjectName(u"result")
        self.result.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(49,50,51);\n"
"	border-radius: 5px\n"
"}")
        self.result.setFrameShape(QFrame.StyledPanel)
        self.result.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.result)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(20, 10, 30, 10)
        self.label_2 = QLabel(self.result)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setFont(font4)

        self.verticalLayout_23.addWidget(self.label_2)

        self.frame_37 = QFrame(self.result)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.api = QLabel(self.frame_37)
        self.api.setObjectName(u"api")
        self.api.setMaximumSize(QSize(30, 30))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setBold(True)
        self.api.setFont(font7)
        self.api.setStyleSheet(u"")
        self.api.setOpenExternalLinks(True)

        self.horizontalLayout_8.addWidget(self.api)

        self.json = QLabel(self.frame_37)
        self.json.setObjectName(u"json")
        self.json.setMaximumSize(QSize(30, 30))
        self.json.setFont(font2)
        self.json.setOpenExternalLinks(False)

        self.horizontalLayout_8.addWidget(self.json)

        self.widget_5 = QWidget(self.frame_37)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background:transparent;\n"
"")

        self.horizontalLayout_8.addWidget(self.widget_5)


        self.verticalLayout_23.addWidget(self.frame_37)

        self.result_table = QTableWidget(self.result)
        if (self.result_table.columnCount() < 4):
            self.result_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.result_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.result_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.result_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.result_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.result_table.rowCount() < 30):
            self.result_table.setRowCount(30)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(43, 43, 43);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(85,85,85);\n"
"}\n"
"QTableCornerButton::section {                                           \n"
"	background: transparent;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QHeaderView::section{\n"
"/*	Background-color: rgb(38,39,43);*/\n"
"	Background-color: rgb(49,50,51);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"/*    border: 1px solid rgb(38,39, 43);*/\n"
"/*	Background-"
                        "color: rgb(38,39,43);*/\n"
" border: 1px solid rgb(49,50,51);\n"
"	Background-color: rgb(49,50,51);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);	\n"
"    min-height: 25px;\n"
"	max-height: 25px;\n"
"	border-radius: 7px;\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"} \n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     heigh"
                        "t: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.result_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.result_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.result_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_table.setProperty("showDropIndicator", False)
        self.result_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.result_table.setTextElideMode(Qt.ElideMiddle)
        self.result_table.setShowGrid(False)
        self.result_table.setGridStyle(Qt.SolidLine)
        self.result_table.setWordWrap(False)
        self.result_table.setCornerButtonEnabled(False)
        self.result_table.setRowCount(30)
        self.result_table.setColumnCount(4)
        self.result_table.horizontalHeader().setVisible(True)
        self.result_table.horizontalHeader().setCascadingSectionResizes(True)
        self.result_table.horizontalHeader().setMinimumSectionSize(50)
        self.result_table.horizontalHeader().setDefaultSectionSize(80)
        self.result_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.result_table.horizontalHeader().setStretchLastSection(False)
        self.result_table.verticalHeader().setVisible(True)
        self.result_table.verticalHeader().setMinimumSectionSize(30)
        self.result_table.verticalHeader().setDefaultSectionSize(30)
        self.result_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_23.addWidget(self.result_table)


        self.horizontalLayout_7.addWidget(self.result)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_3 = QWidget(self.page_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"color: rgb(230, 230, 230);")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.preview = QWidget(self.widget_3)
        self.preview.setObjectName(u"preview")
        self.preview.setStyleSheet(u"background-color: rgb(49,50,51);border-radius: 5px;")
        self.verticalLayout_9 = QVBoxLayout(self.preview)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(30, 10, 30, 30)
        self.label_27 = QLabel(self.preview)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 30))
        self.label_27.setMaximumSize(QSize(16777215, 30))
        self.label_27.setFont(font4)

        self.verticalLayout_9.addWidget(self.label_27)

        self.frame_4 = QFrame(self.preview)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.preview_open_file_label = QLineEdit(self.frame_4)
        self.preview_open_file_label.setObjectName(u"preview_open_file_label")
        self.preview_open_file_label.setMinimumSize(QSize(0, 30))
        self.preview_open_file_label.setFont(font5)
        self.preview_open_file_label.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.preview_open_file_label.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.preview_open_file_label)

        self.preview_open_file_btn = QPushButton(self.frame_4)
        self.preview_open_file_btn.setObjectName(u"preview_open_file_btn")
        self.preview_open_file_btn.setMinimumSize(QSize(120, 30))
        self.preview_open_file_btn.setFont(font)
        self.preview_open_file_btn.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(149,150,151);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton { \n"
"	background-color: rgb(149,150,151);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}")

        self.horizontalLayout_6.addWidget(self.preview_open_file_btn)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_21 = QFrame(self.preview)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.preview_image = QLabel(self.frame_21)
        self.preview_image.setObjectName(u"preview_image")
        self.preview_image.setMinimumSize(QSize(480, 320))
        self.preview_image.setMaximumSize(QSize(640, 480))
        self.preview_image.setStyleSheet(u"background-color: rgb(43,43,43);border-radius: 5px")
        self.preview_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.preview_image)


        self.verticalLayout_9.addWidget(self.frame_21)

        self.Metadata = QFrame(self.preview)
        self.Metadata.setObjectName(u"Metadata")
        self.Metadata.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(80,81,82);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.Metadata.setFrameShape(QFrame.StyledPanel)
        self.Metadata.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Metadata)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.Metadata)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 30))
        self.frame_23.setMaximumSize(QSize(16777215, 30))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.meta_size_lb = QLabel(self.frame_23)
        self.meta_size_lb.setObjectName(u"meta_size_lb")
        self.meta_size_lb.setMinimumSize(QSize(120, 30))
        self.meta_size_lb.setMaximumSize(QSize(16777215, 30))
        self.meta_size_lb.setFont(font7)
        self.meta_size_lb.setStyleSheet(u"")
        self.meta_size_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.meta_size_lb)

        self.meta_size_le = QLineEdit(self.frame_23)
        self.meta_size_le.setObjectName(u"meta_size_le")
        self.meta_size_le.setMinimumSize(QSize(0, 30))
        self.meta_size_le.setMaximumSize(QSize(16777215, 30))
        self.meta_size_le.setFont(font5)
        self.meta_size_le.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.meta_size_le)

        self.meta_nbframe_lb = QLabel(self.frame_23)
        self.meta_nbframe_lb.setObjectName(u"meta_nbframe_lb")
        self.meta_nbframe_lb.setMinimumSize(QSize(120, 30))
        self.meta_nbframe_lb.setMaximumSize(QSize(16777215, 30))
        self.meta_nbframe_lb.setFont(font7)
        self.meta_nbframe_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.meta_nbframe_lb)

        self.meta_nbframe_le = QLineEdit(self.frame_23)
        self.meta_nbframe_le.setObjectName(u"meta_nbframe_le")
        self.meta_nbframe_le.setMinimumSize(QSize(0, 30))
        self.meta_nbframe_le.setMaximumSize(QSize(16777215, 30))
        self.meta_nbframe_le.setFont(font5)
        self.meta_nbframe_le.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.meta_nbframe_le)


        self.verticalLayout_17.addWidget(self.frame_23)

        self.frame_25 = QFrame(self.Metadata)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 30))
        self.frame_25.setMaximumSize(QSize(16777215, 30))
        self.frame_25.setFont(font5)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(120, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFont(font7)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_11)

        self.meta_fps_le = QLineEdit(self.frame_25)
        self.meta_fps_le.setObjectName(u"meta_fps_le")
        self.meta_fps_le.setMinimumSize(QSize(0, 30))
        self.meta_fps_le.setMaximumSize(QSize(16777215, 30))
        self.meta_fps_le.setFont(font5)
        self.meta_fps_le.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.meta_fps_le)

        self.label_16 = QLabel(self.frame_25)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(120, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setFont(font7)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_16)

        self.meta_duration_le = QLineEdit(self.frame_25)
        self.meta_duration_le.setObjectName(u"meta_duration_le")
        self.meta_duration_le.setMinimumSize(QSize(0, 30))
        self.meta_duration_le.setMaximumSize(QSize(16777215, 30))
        self.meta_duration_le.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.meta_duration_le)


        self.verticalLayout_17.addWidget(self.frame_25)

        self.frame_27 = QFrame(self.Metadata)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 30))
        self.frame_27.setMaximumSize(QSize(16777215, 30))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_27)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(120, 30))
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setFont(font7)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_15)

        self.meta_rotate_le = QLineEdit(self.frame_27)
        self.meta_rotate_le.setObjectName(u"meta_rotate_le")
        self.meta_rotate_le.setMinimumSize(QSize(0, 30))
        self.meta_rotate_le.setMaximumSize(QSize(16777215, 30))
        self.meta_rotate_le.setFont(font5)
        self.meta_rotate_le.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.meta_rotate_le)

        self.label_12 = QLabel(self.frame_27)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(120, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font7)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_12)

        self.meta_filesize_le = QLineEdit(self.frame_27)
        self.meta_filesize_le.setObjectName(u"meta_filesize_le")
        self.meta_filesize_le.setMinimumSize(QSize(0, 30))
        self.meta_filesize_le.setMaximumSize(QSize(16777215, 30))
        self.meta_filesize_le.setFont(font5)
        self.meta_filesize_le.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.meta_filesize_le)


        self.verticalLayout_17.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.Metadata)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 30))
        self.frame_28.setMaximumSize(QSize(16777215, 30))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(120, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font7)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_14)

        self.meta_vc_le = QLineEdit(self.frame_28)
        self.meta_vc_le.setObjectName(u"meta_vc_le")
        self.meta_vc_le.setMinimumSize(QSize(0, 30))
        self.meta_vc_le.setMaximumSize(QSize(16777215, 30))
        self.meta_vc_le.setFont(font5)
        self.meta_vc_le.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.meta_vc_le)

        self.label_13 = QLabel(self.frame_28)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(120, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font7)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_13)

        self.meta_ac_le = QLineEdit(self.frame_28)
        self.meta_ac_le.setObjectName(u"meta_ac_le")
        self.meta_ac_le.setMinimumSize(QSize(0, 30))
        self.meta_ac_le.setMaximumSize(QSize(16777215, 30))
        self.meta_ac_le.setFont(font5)
        self.meta_ac_le.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.meta_ac_le)


        self.verticalLayout_17.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.Metadata)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 30))
        self.frame_29.setMaximumSize(QSize(16777215, 30))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_29)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(120, 30))
        self.label_17.setMaximumSize(QSize(120, 30))
        self.label_17.setFont(font7)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_17)

        self.meta_format_le = QLineEdit(self.frame_29)
        self.meta_format_le.setObjectName(u"meta_format_le")
        self.meta_format_le.setMinimumSize(QSize(0, 30))
        self.meta_format_le.setMaximumSize(QSize(16777215, 30))
        self.meta_format_le.setFont(font5)
        self.meta_format_le.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.meta_format_le)


        self.verticalLayout_17.addWidget(self.frame_29)


        self.verticalLayout_9.addWidget(self.Metadata)


        self.horizontalLayout_4.addWidget(self.preview)

        self.controls = QWidget(self.widget_3)
        self.controls.setObjectName(u"controls")
        self.controls.setMaximumSize(QSize(480, 16777215))
        self.controls.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.controls)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.transformation = QWidget(self.controls)
        self.transformation.setObjectName(u"transformation")
        self.transformation.setFont(font7)
        self.transformation.setStyleSheet(u"background-color: rgb(49,50,51);\n"
"border-radius: 5px;")
        self.verticalLayout_12 = QVBoxLayout(self.transformation)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.label_29 = QLabel(self.transformation)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 30))
        self.label_29.setMaximumSize(QSize(16777215, 30))
        self.label_29.setFont(font4)

        self.verticalLayout_12.addWidget(self.label_29)

        self.transform_list = QFrame(self.transformation)
        self.transform_list.setObjectName(u"transform_list")
        self.transform_list.setMinimumSize(QSize(100, 0))
        self.transform_list.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(43,43,43);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(60,60,60,150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/16x16/resource/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgba(80,80,80,150);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(46,46,51);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"   "
                        " margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(49,50,51);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(143,143,143);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(49,50,51);\n"
"	border: 3px solid rgb(49,50,51);	\n"
"	background-image: url(:/icons/16x16/resource/icons/16x16/cil-check-alt.png)\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(49,50,51);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(143,143,143);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    backgr"
                        "ound: 3px solid rgb(49,50,51);\n"
"    border: 3px solid rgb(49,50,51);	\n"
"    background-image: url(:/icons/16x16/resource/icons/16x16/cil-check-alt.png)\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    border: 3px solid rgb(49,50,51);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(143,143,143);\n"
"}\n"
"QGroupBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QGroupBox::indicator:checked {\n"
"    background: 3px solid rgb(49,50,51);\n"
"    border: 3px solid rgb(49,50,51);	\n"
"    background-image: url(:/icons/16x16/resource/icons/16x16/cil-check-alt.png)\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}")
        self.transform_list.setFrameShape(QFrame.StyledPanel)
        self.transform_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.transform_list)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.transform_list)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(60, 0))
        self.label_30.setMaximumSize(QSize(60, 16777215))
        self.label_30.setFont(font7)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_30)

        self.bright_combo = QComboBox(self.frame)
        self.bright_combo.addItem("")
        self.bright_combo.addItem("")
        self.bright_combo.addItem("")
        self.bright_combo.addItem("")
        self.bright_combo.addItem("")
        self.bright_combo.addItem("")
        self.bright_combo.addItem("")
        self.bright_combo.setObjectName(u"bright_combo")
        self.bright_combo.setFont(font5)
        self.bright_combo.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.bright_combo)

        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(60, 0))
        self.label_31.setMaximumSize(QSize(60, 16777215))
        self.label_31.setFont(font7)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_31)

        self.contrast_combo = QComboBox(self.frame)
        self.contrast_combo.addItem("")
        self.contrast_combo.addItem("")
        self.contrast_combo.addItem("")
        self.contrast_combo.setObjectName(u"contrast_combo")
        self.contrast_combo.setFont(font5)

        self.horizontalLayout_5.addWidget(self.contrast_combo)


        self.verticalLayout_13.addWidget(self.frame)

        self.frame_5 = QFrame(self.transform_list)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(60, 0))
        self.label_34.setMaximumSize(QSize(60, 16777215))
        self.label_34.setFont(font7)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_34)

        self.rotate_combo = QComboBox(self.frame_5)
        self.rotate_combo.addItem("")
        self.rotate_combo.addItem("")
        self.rotate_combo.addItem("")
        self.rotate_combo.addItem("")
        self.rotate_combo.setObjectName(u"rotate_combo")
        self.rotate_combo.setFont(font5)

        self.horizontalLayout_11.addWidget(self.rotate_combo)

        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(60, 0))
        self.label_35.setMaximumSize(QSize(60, 16777215))
        self.label_35.setFont(font7)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_35)

        self.flip_combo = QComboBox(self.frame_5)
        self.flip_combo.addItem("")
        self.flip_combo.addItem("")
        self.flip_combo.addItem("")
        self.flip_combo.addItem("")
        self.flip_combo.setObjectName(u"flip_combo")
        self.flip_combo.setFont(font5)

        self.horizontalLayout_11.addWidget(self.flip_combo)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.transform_list)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(60, 0))
        self.label_18.setMaximumSize(QSize(60, 16777215))
        self.label_18.setFont(font7)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_18)

        self.fps_combo = QComboBox(self.frame_3)
        self.fps_combo.addItem("")
        self.fps_combo.addItem("")
        self.fps_combo.addItem("")
        self.fps_combo.addItem("")
        self.fps_combo.setObjectName(u"fps_combo")
        self.fps_combo.setFont(font5)

        self.horizontalLayout_10.addWidget(self.fps_combo)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(60, 0))
        self.label_10.setMaximumSize(QSize(60, 16777215))
        self.label_10.setFont(font7)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.gray_combo = QComboBox(self.frame_3)
        self.gray_combo.addItem("")
        self.gray_combo.addItem("")
        self.gray_combo.setObjectName(u"gray_combo")
        self.gray_combo.setFont(font5)

        self.horizontalLayout_10.addWidget(self.gray_combo)


        self.verticalLayout_13.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.transform_list)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.crop_check = QCheckBox(self.frame_6)
        self.crop_check.setObjectName(u"crop_check")
        self.crop_check.setMinimumSize(QSize(120, 0))
        self.crop_check.setMaximumSize(QSize(40, 16777215))
        self.crop_check.setFont(font7)

        self.horizontalLayout_13.addWidget(self.crop_check)

        self.crop_label = QLabel(self.frame_6)
        self.crop_label.setObjectName(u"crop_label")
        self.crop_label.setMinimumSize(QSize(40, 0))
        self.crop_label.setFont(font5)
        self.crop_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.crop_label)

        self.crop_slider = QSlider(self.frame_6)
        self.crop_slider.setObjectName(u"crop_slider")
        self.crop_slider.setMaximum(10)
        self.crop_slider.setSingleStep(1)
        self.crop_slider.setPageStep(1)
        self.crop_slider.setOrientation(Qt.Horizontal)
        self.crop_slider.setTickInterval(5)

        self.horizontalLayout_13.addWidget(self.crop_slider)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.transform_list)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.border_check = QCheckBox(self.frame_7)
        self.border_check.setObjectName(u"border_check")
        self.border_check.setMinimumSize(QSize(120, 0))
        self.border_check.setFont(font7)

        self.horizontalLayout_14.addWidget(self.border_check)

        self.border_w_label = QLabel(self.frame_7)
        self.border_w_label.setObjectName(u"border_w_label")
        self.border_w_label.setMinimumSize(QSize(40, 0))
        self.border_w_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.border_w_label)

        self.border_w_slider = QSlider(self.frame_7)
        self.border_w_slider.setObjectName(u"border_w_slider")
        self.border_w_slider.setMinimum(0)
        self.border_w_slider.setMaximum(10)
        self.border_w_slider.setSingleStep(1)
        self.border_w_slider.setPageStep(1)
        self.border_w_slider.setValue(0)
        self.border_w_slider.setOrientation(Qt.Horizontal)
        self.border_w_slider.setTickInterval(5)

        self.horizontalLayout_14.addWidget(self.border_w_slider)

        self.border_h_label = QLabel(self.frame_7)
        self.border_h_label.setObjectName(u"border_h_label")
        self.border_h_label.setMinimumSize(QSize(40, 0))
        self.border_h_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.border_h_label)

        self.border_h_slider = QSlider(self.frame_7)
        self.border_h_slider.setObjectName(u"border_h_slider")
        self.border_h_slider.setMaximum(10)
        self.border_h_slider.setSingleStep(1)
        self.border_h_slider.setPageStep(1)
        self.border_h_slider.setOrientation(Qt.Horizontal)
        self.border_h_slider.setTickInterval(5)

        self.horizontalLayout_14.addWidget(self.border_h_slider)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.transform_list)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.res_check = QCheckBox(self.frame_9)
        self.res_check.setObjectName(u"res_check")
        self.res_check.setFont(font7)

        self.verticalLayout_15.addWidget(self.res_check)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_10)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font5)
        self.groupBox.setFlat(False)
        self.verticalLayout_19 = QVBoxLayout(self.groupBox)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(20, 0, 0, 0)
        self.res_preset_rb = QRadioButton(self.groupBox)
        self.res_preset_rb.setObjectName(u"res_preset_rb")
        self.res_preset_rb.setMinimumSize(QSize(100, 22))
        self.res_preset_rb.setFont(font5)

        self.verticalLayout_19.addWidget(self.res_preset_rb)

        self.res_ratio_rb = QRadioButton(self.groupBox)
        self.res_ratio_rb.setObjectName(u"res_ratio_rb")
        self.res_ratio_rb.setMinimumSize(QSize(100, 22))
        self.res_ratio_rb.setFont(font5)

        self.verticalLayout_19.addWidget(self.res_ratio_rb)


        self.horizontalLayout_30.addWidget(self.groupBox)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 0, 0, 0)
        self.res_preset_combo = QComboBox(self.frame_14)
        self.res_preset_combo.addItem("")
        self.res_preset_combo.addItem("")
        self.res_preset_combo.addItem("")
        self.res_preset_combo.addItem("")
        self.res_preset_combo.setObjectName(u"res_preset_combo")
        self.res_preset_combo.setFont(font5)

        self.verticalLayout_18.addWidget(self.res_preset_combo)

        self.res_ratio_slider = QSlider(self.frame_14)
        self.res_ratio_slider.setObjectName(u"res_ratio_slider")
        self.res_ratio_slider.setMinimum(-6)
        self.res_ratio_slider.setMaximum(6)
        self.res_ratio_slider.setSingleStep(1)
        self.res_ratio_slider.setPageStep(1)
        self.res_ratio_slider.setValue(0)
        self.res_ratio_slider.setOrientation(Qt.Horizontal)
        self.res_ratio_slider.setInvertedAppearance(False)
        self.res_ratio_slider.setInvertedControls(False)
        self.res_ratio_slider.setTickPosition(QSlider.NoTicks)
        self.res_ratio_slider.setTickInterval(5)

        self.verticalLayout_18.addWidget(self.res_ratio_slider)


        self.horizontalLayout_30.addWidget(self.frame_14)


        self.verticalLayout_15.addWidget(self.frame_10)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_13 = QFrame(self.transform_list)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_13)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pip_check = QCheckBox(self.frame_26)
        self.pip_check.setObjectName(u"pip_check")
        self.pip_check.setMinimumSize(QSize(120, 22))
        self.pip_check.setFont(font7)

        self.horizontalLayout_9.addWidget(self.pip_check)

        self.pip_file_le = QLineEdit(self.frame_26)
        self.pip_file_le.setObjectName(u"pip_file_le")
        self.pip_file_le.setMinimumSize(QSize(0, 22))
        self.pip_file_le.setFont(font5)
        self.pip_file_le.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.pip_file_le)

        self.pip_file_open_btn = QToolButton(self.frame_26)
        self.pip_file_open_btn.setObjectName(u"pip_file_open_btn")
        self.pip_file_open_btn.setMinimumSize(QSize(22, 22))
        icon6 = QIcon()
        icon6.addFile(u":/icons/16x16/resource/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pip_file_open_btn.setIcon(icon6)

        self.horizontalLayout_9.addWidget(self.pip_file_open_btn)

        self.pip_file_reset_btn = QToolButton(self.frame_26)
        self.pip_file_reset_btn.setObjectName(u"pip_file_reset_btn")
        self.pip_file_reset_btn.setMinimumSize(QSize(22, 22))
        icon7 = QIcon()
        icon7.addFile(u":/icons/16x16/resource/icons/16x16/cil-image1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pip_file_reset_btn.setIcon(icon7)

        self.horizontalLayout_9.addWidget(self.pip_file_reset_btn)


        self.verticalLayout_20.addWidget(self.frame_26)

        self.frame_20 = QFrame(self.frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pip_ratio_label = QLabel(self.frame_20)
        self.pip_ratio_label.setObjectName(u"pip_ratio_label")
        self.pip_ratio_label.setMinimumSize(QSize(120, 22))
        self.pip_ratio_label.setMaximumSize(QSize(80, 16777215))
        self.pip_ratio_label.setFont(font5)
        self.pip_ratio_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.pip_ratio_label)

        self.pip_ratio_slider = QSlider(self.frame_20)
        self.pip_ratio_slider.setObjectName(u"pip_ratio_slider")
        self.pip_ratio_slider.setMinimum(0)
        self.pip_ratio_slider.setMaximum(20)
        self.pip_ratio_slider.setSingleStep(1)
        self.pip_ratio_slider.setPageStep(1)
        self.pip_ratio_slider.setValue(0)
        self.pip_ratio_slider.setOrientation(Qt.Horizontal)
        self.pip_ratio_slider.setTickInterval(5)

        self.horizontalLayout_16.addWidget(self.pip_ratio_slider)


        self.verticalLayout_20.addWidget(self.frame_20)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_8 = QFrame(self.transform_list)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.logo_check = QCheckBox(self.frame_16)
        self.logo_check.setObjectName(u"logo_check")
        self.logo_check.setMinimumSize(QSize(120, 22))
        self.logo_check.setFont(font7)

        self.horizontalLayout_17.addWidget(self.logo_check)

        self.logo_file_le = QLineEdit(self.frame_16)
        self.logo_file_le.setObjectName(u"logo_file_le")
        self.logo_file_le.setMinimumSize(QSize(0, 22))
        self.logo_file_le.setFont(font5)
        self.logo_file_le.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.logo_file_le)

        self.logo_file_open_btn = QToolButton(self.frame_16)
        self.logo_file_open_btn.setObjectName(u"logo_file_open_btn")
        self.logo_file_open_btn.setMinimumSize(QSize(22, 22))
        self.logo_file_open_btn.setIcon(icon6)

        self.horizontalLayout_17.addWidget(self.logo_file_open_btn)

        self.logo_file_reset_btn = QToolButton(self.frame_16)
        self.logo_file_reset_btn.setObjectName(u"logo_file_reset_btn")
        self.logo_file_reset_btn.setMinimumSize(QSize(22, 22))
        self.logo_file_reset_btn.setIcon(icon7)

        self.horizontalLayout_17.addWidget(self.logo_file_reset_btn)


        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_22 = QFrame(self.frame_8)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.logo_size_label = QLabel(self.frame_22)
        self.logo_size_label.setObjectName(u"logo_size_label")
        self.logo_size_label.setMinimumSize(QSize(120, 22))
        self.logo_size_label.setFont(font5)
        self.logo_size_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.logo_size_label)

        self.logo_size_slider = QSlider(self.frame_22)
        self.logo_size_slider.setObjectName(u"logo_size_slider")
        self.logo_size_slider.setMaximum(10)
        self.logo_size_slider.setSingleStep(1)
        self.logo_size_slider.setPageStep(1)
        self.logo_size_slider.setOrientation(Qt.Horizontal)
        self.logo_size_slider.setTickInterval(5)

        self.horizontalLayout_18.addWidget(self.logo_size_slider)


        self.verticalLayout_14.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.frame_8)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_24)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 22))
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_4)

        self.logo_pos_x_label = QLabel(self.frame_24)
        self.logo_pos_x_label.setObjectName(u"logo_pos_x_label")
        self.logo_pos_x_label.setMinimumSize(QSize(40, 0))
        self.logo_pos_x_label.setFont(font5)
        self.logo_pos_x_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.logo_pos_x_label)

        self.logo_pos_x_slider = QSlider(self.frame_24)
        self.logo_pos_x_slider.setObjectName(u"logo_pos_x_slider")
        self.logo_pos_x_slider.setMaximum(20)
        self.logo_pos_x_slider.setSingleStep(1)
        self.logo_pos_x_slider.setPageStep(1)
        self.logo_pos_x_slider.setValue(0)
        self.logo_pos_x_slider.setOrientation(Qt.Horizontal)
        self.logo_pos_x_slider.setTickInterval(5)

        self.horizontalLayout_22.addWidget(self.logo_pos_x_slider)

        self.logo_pos_y_label = QLabel(self.frame_24)
        self.logo_pos_y_label.setObjectName(u"logo_pos_y_label")
        self.logo_pos_y_label.setMinimumSize(QSize(40, 0))
        self.logo_pos_y_label.setFont(font5)
        self.logo_pos_y_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.logo_pos_y_label)

        self.logo_pos_y_slider = QSlider(self.frame_24)
        self.logo_pos_y_slider.setObjectName(u"logo_pos_y_slider")
        self.logo_pos_y_slider.setMaximum(20)
        self.logo_pos_y_slider.setSingleStep(1)
        self.logo_pos_y_slider.setPageStep(1)
        self.logo_pos_y_slider.setValue(0)
        self.logo_pos_y_slider.setOrientation(Qt.Horizontal)
        self.logo_pos_y_slider.setTickInterval(5)

        self.horizontalLayout_22.addWidget(self.logo_pos_y_slider)


        self.verticalLayout_14.addWidget(self.frame_24)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.frame_18 = QFrame(self.transform_list)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_18)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.caption_check = QCheckBox(self.frame_11)
        self.caption_check.setObjectName(u"caption_check")
        self.caption_check.setMinimumSize(QSize(120, 22))
        self.caption_check.setFont(font7)

        self.horizontalLayout_19.addWidget(self.caption_check)

        self.caption_text_le = QLineEdit(self.frame_11)
        self.caption_text_le.setObjectName(u"caption_text_le")
        self.caption_text_le.setMinimumSize(QSize(0, 22))
        self.caption_text_le.setFont(font5)

        self.horizontalLayout_19.addWidget(self.caption_text_le)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.caption_label = QLabel(self.frame_17)
        self.caption_label.setObjectName(u"caption_label")
        self.caption_label.setMinimumSize(QSize(0, 22))
        self.caption_label.setMaximumSize(QSize(120, 16777215))
        self.caption_label.setFont(font5)
        self.caption_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.caption_label)

        self.caption_color = QLabel(self.frame_17)
        self.caption_color.setObjectName(u"caption_color")
        self.caption_color.setMaximumSize(QSize(0, 16777215))

        self.horizontalLayout_20.addWidget(self.caption_color)

        self.caption_font_label = QLabel(self.frame_17)
        self.caption_font_label.setObjectName(u"caption_font_label")
        self.caption_font_label.setMaximumSize(QSize(275, 22))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(12)
        self.caption_font_label.setFont(font8)
        self.caption_font_label.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(80,80,80,150);\n"
"	border-radius: 5px;\n"
"}\n"
"QLabel:hover {\n"
"border: 2px solid rgb(64, 71, 88);\n"
"};\n"
"")
        self.caption_font_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.caption_font_label)

        self.frame_15 = QFrame(self.frame_17)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(50, 22))
        self.frame_15.setStyleSheet(u"QLabel{\n"
"	background-color:  #0000ff;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"QLabel:hover {\n"
"border: 2px solid rgb(64, 71, 88);\n"
"};\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.caption_color_label = QLabel(self.frame_15)
        self.caption_color_label.setObjectName(u"caption_color_label")
        self.caption_color_label.setMaximumSize(QSize(50, 22))
        self.caption_color_label.setFont(font5)
        self.caption_color_label.setStyleSheet(u"background-color:  #000000;\n"
"")

        self.horizontalLayout_12.addWidget(self.caption_color_label)


        self.horizontalLayout_20.addWidget(self.frame_15)


        self.verticalLayout_21.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 22))
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_7)

        self.caption_x_label = QLabel(self.frame_19)
        self.caption_x_label.setObjectName(u"caption_x_label")
        self.caption_x_label.setMinimumSize(QSize(40, 0))
        self.caption_x_label.setFont(font5)
        self.caption_x_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.caption_x_label)

        self.caption_x_slider = QSlider(self.frame_19)
        self.caption_x_slider.setObjectName(u"caption_x_slider")
        self.caption_x_slider.setMaximum(20)
        self.caption_x_slider.setSingleStep(1)
        self.caption_x_slider.setPageStep(1)
        self.caption_x_slider.setOrientation(Qt.Horizontal)
        self.caption_x_slider.setTickInterval(5)

        self.horizontalLayout_21.addWidget(self.caption_x_slider)

        self.caption_y_label = QLabel(self.frame_19)
        self.caption_y_label.setObjectName(u"caption_y_label")
        self.caption_y_label.setMinimumSize(QSize(40, 0))
        self.caption_y_label.setFont(font5)
        self.caption_y_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.caption_y_label)

        self.caption_y_slider = QSlider(self.frame_19)
        self.caption_y_slider.setObjectName(u"caption_y_slider")
        self.caption_y_slider.setMaximum(20)
        self.caption_y_slider.setSingleStep(1)
        self.caption_y_slider.setPageStep(1)
        self.caption_y_slider.setOrientation(Qt.Horizontal)
        self.caption_y_slider.setTickInterval(5)

        self.horizontalLayout_21.addWidget(self.caption_y_slider)


        self.verticalLayout_21.addWidget(self.frame_19)


        self.verticalLayout_13.addWidget(self.frame_18)


        self.verticalLayout_12.addWidget(self.transform_list)


        self.verticalLayout_11.addWidget(self.transformation)

        self.Submit = QFrame(self.controls)
        self.Submit.setObjectName(u"Submit")
        self.Submit.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(149,150,151);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPushButton:disabled{\n"
"	border: 2px solid rgb(80, 80, 80);\n"
"}")
        self.Submit.setFrameShape(QFrame.StyledPanel)
        self.Submit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.Submit)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 60, 0, 0)
        self.widget_4 = QWidget(self.Submit)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout_23.addWidget(self.widget_4)

        self.reset_trn_btn = QPushButton(self.Submit)
        self.reset_trn_btn.setObjectName(u"reset_trn_btn")
        self.reset_trn_btn.setMinimumSize(QSize(0, 30))
        self.reset_trn_btn.setMaximumSize(QSize(120, 16777215))
        self.reset_trn_btn.setFont(font)

        self.horizontalLayout_23.addWidget(self.reset_trn_btn)

        self.save_trn_btn = QPushButton(self.Submit)
        self.save_trn_btn.setObjectName(u"save_trn_btn")
        self.save_trn_btn.setMinimumSize(QSize(0, 30))
        self.save_trn_btn.setMaximumSize(QSize(120, 16777215))
        self.save_trn_btn.setFont(font)

        self.horizontalLayout_23.addWidget(self.save_trn_btn)

        self.detect_trn_btn = QPushButton(self.Submit)
        self.detect_trn_btn.setObjectName(u"detect_trn_btn")
        self.detect_trn_btn.setMinimumSize(QSize(0, 30))
        self.detect_trn_btn.setMaximumSize(QSize(120, 16777215))
        self.detect_trn_btn.setFont(font)

        self.horizontalLayout_23.addWidget(self.detect_trn_btn)


        self.verticalLayout_11.addWidget(self.Submit)


        self.horizontalLayout_4.addWidget(self.controls)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.content)


        self.horizontalLayout_3.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.bright_combo.setCurrentIndex(3)
        self.contrast_combo.setCurrentIndex(1)
        self.res_preset_combo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sidenav_title_label.setText("")
        self.page_1_btn.setText("")
        self.page_2_btn.setText("")
        self.btn_setting.setText("")
        self.win_title_label.setText(QCoreApplication.translate("MainWindow", u"Partial Copy Detection ", None))
        self.win_minimize_btn.setText("")
        self.win_maximize_btn.setText("")
        self.win_close_btn.setText("")
        self.page_header.setText(QCoreApplication.translate("MainWindow", u"page header", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Query", None))
        self.query_open_le.setText("")
        self.query_open_btn.setText(QCoreApplication.translate("MainWindow", u"Open Video", None))
        self.query_image.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Top K", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Score Threshold", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Match Threshold", None))
        self.query_topk_label.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.query_wnd_label.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.query_score_thr_label.setText(QCoreApplication.translate("MainWindow", u"0.6", None))
        self.query_match_thr_label.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.query_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.query_submit_btn.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Detected", None))
        self.api.setText(QCoreApplication.translate("MainWindow", u"<a href=\"http://mltigers.sogang.ac.kr:8777/api/query/\" style=\"color: rgb(230,230,230);\">API</a>", None))
        self.json.setText(QCoreApplication.translate("MainWindow", u"<a href=\"http://mltigers.sogang.ac.kr:8777/api/query/?format=json\" style=\"color: rgb(230,230,230);\">JSON</a>", None))
        ___qtablewidgetitem = self.result_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.result_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem2 = self.result_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Score", None));
        ___qtablewidgetitem3 = self.result_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Match", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.preview_open_file_btn.setText(QCoreApplication.translate("MainWindow", u"Open Video", None))
        self.preview_image.setText("")
        self.meta_size_lb.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.meta_size_le.setText("")
        self.meta_nbframe_lb.setText(QCoreApplication.translate("MainWindow", u"Frame Count", None))
        self.meta_nbframe_le.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"File Size", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Video Codec", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Audio Codec", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Transformations", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\ubc1d\uae30", None))
        self.bright_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"-36", None))
        self.bright_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"-18", None))
        self.bright_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"-9", None))
        self.bright_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"0", None))
        self.bright_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"9", None))
        self.bright_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"18", None))
        self.bright_combo.setItemText(6, QCoreApplication.translate("MainWindow", u"36", None))

        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\ub300\uc870", None))
        self.contrast_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"-20", None))
        self.contrast_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.contrast_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\ud68c\uc804", None))
        self.rotate_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.rotate_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"90", None))
        self.rotate_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"180", None))
        self.rotate_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"270", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\ubc18\uc804", None))
        self.flip_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.flip_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Horizontal", None))
        self.flip_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Vertical", None))
        self.flip_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"ALL", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.fps_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.fps_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"5 fps", None))
        self.fps_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"10 fps", None))
        self.fps_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"20 fps", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\ud751\ubc31", None))
        self.gray_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"OFF", None))
        self.gray_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"ON", None))

        self.crop_check.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.crop_label.setText(QCoreApplication.translate("MainWindow", u"Ratio", None))
        self.border_check.setText(QCoreApplication.translate("MainWindow", u"Border", None))
        self.border_w_label.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.border_h_label.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.res_check.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.groupBox.setTitle("")
        self.res_preset_rb.setText(QCoreApplication.translate("MainWindow", u"Preset", None))
        self.res_ratio_rb.setText(QCoreApplication.translate("MainWindow", u"Ratio", None))
        self.res_preset_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.res_preset_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"QCIF", None))
        self.res_preset_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"CIF", None))
        self.res_preset_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"SD", None))

        self.pip_check.setText(QCoreApplication.translate("MainWindow", u"PIP", None))
        self.pip_file_open_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pip_file_reset_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pip_ratio_label.setText(QCoreApplication.translate("MainWindow", u"Ratio", None))
        self.logo_check.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.logo_file_open_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.logo_file_reset_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.logo_size_label.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pos", None))
        self.logo_pos_x_label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.logo_pos_y_label.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.caption_check.setText(QCoreApplication.translate("MainWindow", u"Caption", None))
        self.caption_label.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.caption_color.setText(QCoreApplication.translate("MainWindow", u"#000000", None))
        self.caption_font_label.setText(QCoreApplication.translate("MainWindow", u"Segoe UI, 24", None))
        self.caption_color_label.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pos", None))
        self.caption_x_label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.caption_y_label.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.reset_trn_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.save_trn_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.detect_trn_btn.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
    # retranslateUi

