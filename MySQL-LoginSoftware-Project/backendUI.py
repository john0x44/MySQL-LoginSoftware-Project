##  Name: backendUI
##  Copyright: © 2023 John0x44. All rights reserved.
##  Author: John0x44
##  Date: 21/06/23 18:10
##  Description: Auto generated PySide2 file by QTDesigner 

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(874, 328)
        MainWindow.setFixedSize(874,328)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #1c1a27;\n"
"color: white;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.TitleFrame = QFrame(self.frame_2)
        self.TitleFrame.setObjectName(u"TitleFrame")
        self.TitleFrame.setMaximumSize(QSize(16777215, 80))
        self.TitleFrame.setStyleSheet(u"")
        self.TitleFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TitleFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon = QPushButton(self.TitleFrame)
        self.icon.setObjectName(u"icon")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMaximumSize(QSize(50, 16777215))
        self.icon.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"border-bottom: 1px solid rgba(255,255,255,23)")
        icon1 = QIcon()
        icon1.addFile(u"./softwareIcons/signal [#1518].svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon1)
        self.icon.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.icon)

        self.label = QLabel(self.TitleFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"Border:0px;\n"
"border-bottom: 1px solid rgba(255,255,255,23)")

        self.horizontalLayout.addWidget(self.label)

        self.filler = QLabel(self.TitleFrame)
        self.filler.setObjectName(u"filler")
        self.filler.setMinimumSize(QSize(610, 0))

        self.horizontalLayout.addWidget(self.filler)


        self.verticalLayout_3.addWidget(self.TitleFrame)

        self.usernameFrame = QFrame(self.frame_2)
        self.usernameFrame.setObjectName(u"usernameFrame")
        self.usernameFrame.setMinimumSize(QSize(300, 0))
        self.usernameFrame.setMaximumSize(QSize(16777215, 45))
        self.usernameFrame.setStyleSheet(u"Border: 1px solid rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.usernameFrame.setFrameShape(QFrame.StyledPanel)
        self.usernameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.usernameFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.pushButton = QPushButton(self.usernameFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMaximumSize(QSize(50, 16777215))
        self.pushButton.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./softwareIcons/profile [#1336].svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.usernameInput = QLineEdit(self.usernameFrame)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy1.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.usernameInput.setFont(font1)
        self.usernameInput.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")

        self.horizontalLayout_2.addWidget(self.usernameInput)


        self.verticalLayout_3.addWidget(self.usernameFrame, 0, Qt.AlignHCenter)

        self.passwordFrame = QFrame(self.frame_2)
        self.passwordFrame.setObjectName(u"passwordFrame")
        self.passwordFrame.setMinimumSize(QSize(300, 0))
        self.passwordFrame.setMaximumSize(QSize(16777215, 45))
        self.passwordFrame.setStyleSheet(u"Border: 1px solid rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.passwordFrame.setFrameShape(QFrame.StyledPanel)
        self.passwordFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.passwordFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_2 = QPushButton(self.passwordFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))
        self.pushButton_2.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./softwareIcons/lock_close [#705].svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.passwordInput = QLineEdit(self.passwordFrame)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy1.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy1)
        self.passwordInput.setFont(font1)
        self.passwordInput.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")

        self.horizontalLayout_3.addWidget(self.passwordInput)


        self.verticalLayout_3.addWidget(self.passwordFrame, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(315, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LoginButton = QPushButton(self.frame_6)
        self.LoginButton.setObjectName(u"LoginButton")
        sizePolicy.setHeightForWidth(self.LoginButton.sizePolicy().hasHeightForWidth())
        self.LoginButton.setSizePolicy(sizePolicy)
        self.LoginButton.setMaximumSize(QSize(100, 16777215))
        self.LoginButton.setFont(font1)
        self.LoginButton.setStyleSheet(u"*{background-color: #18A558;\n"
"Border: 0px;\n"
"color: black;\n"
"Border-radius: 5px;\n"
"}\n"
"QPushButton:Hover{background-color: #56CC87}")

        self.horizontalLayout_4.addWidget(self.LoginButton)

        self.LoginState = QLabel(self.frame_6)
        self.LoginState.setObjectName(u"LoginState")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setItalic(True)
        self.LoginState.setFont(font2)
        self.LoginState.setStyleSheet(u"color: rgba(255,255,255, 75)")
        self.LoginState.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.LoginState)


        self.verticalLayout_3.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 45))
        self.frame_3.setStyleSheet(u"Border-top: 1px solid rgba(255,255,255,42);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"Border-top: 0px")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.WelcomeLabel = QPushButton(self.frame_5)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        sizePolicy1.setHeightForWidth(self.WelcomeLabel.sizePolicy().hasHeightForWidth())
        self.WelcomeLabel.setSizePolicy(sizePolicy1)
        self.WelcomeLabel.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.WelcomeLabel.setFont(font3)
        self.WelcomeLabel.setStyleSheet(u"Border:0px")
        self.WelcomeLabel.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.WelcomeLabel)


        self.horizontalLayout_6.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(200, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.DatabaseLabel = QPushButton(self.frame_8)
        self.DatabaseLabel.setObjectName(u"DatabaseLabel")
        sizePolicy1.setHeightForWidth(self.DatabaseLabel.sizePolicy().hasHeightForWidth())
        self.DatabaseLabel.setSizePolicy(sizePolicy1)
        self.DatabaseLabel.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        self.DatabaseLabel.setFont(font4)
        self.DatabaseLabel.setLayoutDirection(Qt.LeftToRight)
        self.DatabaseLabel.setStyleSheet(u"Border:0px")
        icon4 = QIcon()
        icon4.addFile(u"./softwareIcons/database_system [#1800].svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DatabaseLabel.setIcon(icon4)

        self.horizontalLayout_8.addWidget(self.DatabaseLabel)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(110, 0))
        self.frame_7.setMaximumSize(QSize(0, 16777215))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.RegisterButton = QPushButton(self.frame_7)
        self.RegisterButton.setObjectName(u"RegisterButton")
        sizePolicy1.setHeightForWidth(self.RegisterButton.sizePolicy().hasHeightForWidth())
        self.RegisterButton.setSizePolicy(sizePolicy1)
        self.RegisterButton.setMinimumSize(QSize(0, 30))
        self.RegisterButton.setMaximumSize(QSize(200, 16777215))
        self.RegisterButton.setFont(font3)
        self.RegisterButton.setStyleSheet(u"*{background-color: #292631;\n"
"Border: 0px;\n"
"color: white;\n"
"Border-radius: 5px}\n"
"QPushButton:Hover{background-color: gray}")
        icon5 = QIcon()
        icon5.addFile(u"./softwareIcons/file_arrow_down [#1613].svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RegisterButton.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.RegisterButton)


        self.horizontalLayout_6.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.frame_4, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"CompanyXYZ Login ", None))
        self.filler.setText("")
        self.pushButton.setText("")
        self.usernameInput.setText("")
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.pushButton_2.setText("")
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.LoginState.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.WelcomeLabel.setText("")
        self.DatabaseLabel.setText(QCoreApplication.translate("MainWindow", u"Database Connected: True", None))
        self.RegisterButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
    # retranslateUi

