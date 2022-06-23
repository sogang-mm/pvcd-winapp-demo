# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_transform_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(622, 300)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(60,63,65);\n"
"	color: rgb(230,230,230);\n"
"}\n"
"QLabel{\n"
"	background: transparent;\n"
"	color: rgb(230,230,230);\n"
"}\n"
"QProgressBar{\n"
"    background-color: rgb(79,82,84);\n"
"	color: rgb(230,230,230);\n"
"	border-radius: 5px;\n"
"	 text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(105,180,255);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgb(43,43,43);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	color: rgb(230,230,230);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
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
"	border-radius: 7px;\n"
"    border: n"
                        "one;\n"
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
"     height: 20px;\n"
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
"     background: n"
                        "one;\n"
" }\n"
"QPushButton { \n"
"	background-color: rgb(149,150,151);\n"
"	border-radius: 5px;\n"
"	color:rgb(230,230,230);\n"
"}\n"
"QPushButton:hover{ \n"
"border: 2px solid rgb(64, 71, 88);\n"
"}")
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(Dialog)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dialog_header = QLabel(self.header)
        self.dialog_header.setObjectName(u"dialog_header")
        self.dialog_header.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.dialog_header.setFont(font1)
        self.dialog_header.setStyleSheet(u"background-color:rgb(43,43,43);\n"
"")
        self.dialog_header.setMargin(10)

        self.verticalLayout_2.addWidget(self.dialog_header)


        self.verticalLayout.addWidget(self.header)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 30, 20, 10)
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.progressBar.setFont(font2)
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 80))
        self.label.setMaximumSize(QSize(60, 80))
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.command_te = QPlainTextEdit(self.frame)
        self.command_te.setObjectName(u"command_te")
        self.command_te.setMinimumSize(QSize(0, 100))
        self.command_te.setMaximumSize(QSize(16777215, 100))
        self.command_te.setReadOnly(True)

        self.horizontalLayout.addWidget(self.command_te)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(100, -1, 20, -1)
        self.log_label = QLabel(self.frame_2)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setMinimumSize(QSize(500, 20))
        self.log_label.setMaximumSize(QSize(500, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.log_label.setFont(font3)
        self.log_label.setStyleSheet(u"color:rgb(230,230,230);\n"
"")

        self.verticalLayout_3.addWidget(self.log_label)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout_4.addWidget(self.widget)

        self.close_btn = QPushButton(self.frame_4)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setEnabled(True)
        self.close_btn.setMinimumSize(QSize(120, 30))
        self.close_btn.setMaximumSize(QSize(120, 30))
        self.close_btn.setFont(font2)
        self.close_btn.setStyleSheet(u"QPushButton:disabled {\n"
"	background-color:rgb(80,80,80);\n"
"}")

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Converting Video", None))
        self.dialog_header.setText(QCoreApplication.translate("Dialog", u"Converting Video...", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Command", None))
        self.log_label.setText(QCoreApplication.translate("Dialog", u"Log: ", None))
        self.close_btn.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

