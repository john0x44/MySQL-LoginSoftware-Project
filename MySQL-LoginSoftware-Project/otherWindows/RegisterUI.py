##  Name: main
##  Copyright: © 2023 John0x44. All rights reserved.
##  Author: John0x44
##  Date: 21/06/23 18:10
##  Description: Auto generated PySide2 file by QTDesigner 

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class RegisterUI(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        if not self.MainWindow.objectName():
            self.MainWindow.setObjectName(u"MainWindow")
        self.MainWindow.resize(733, 336)
        self.MainWindow.setFixedSize(733,336)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #1c1a27;\n"
    "color: white;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(160, 30))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"Border:0px;\n"
"border-bottom: 1px solid rgba(255,255,255,23)")

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.nameFrame = QFrame(self.frame_4)
        self.nameFrame.setObjectName(u"nameFrame")
        self.nameFrame.setMinimumSize(QSize(250, 0))
        self.nameFrame.setMaximumSize(QSize(16777215, 55))
        self.nameFrame.setStyleSheet(u"Border: 1px solid rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.nameFrame.setFrameShape(QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.nameFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_6 = QPushButton(self.nameFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QSize(50, 16777215))
        self.pushButton_6.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")
        icon = QIcon()
        icon.addFile(u"./otherWindows/profile [#1336].svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.nameInput = QLineEdit(self.nameFrame)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        self.nameInput.setFont(font1)
        self.nameInput.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")

        self.horizontalLayout_5.addWidget(self.nameInput)


        self.horizontalLayout_6.addWidget(self.nameFrame)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.usernameFrame = QFrame(self.frame_5)
        self.usernameFrame.setObjectName(u"usernameFrame")
        self.usernameFrame.setMinimumSize(QSize(250, 0))
        self.usernameFrame.setMaximumSize(QSize(16777215, 55))
        self.usernameFrame.setStyleSheet(u"Border: 1px solid rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.usernameFrame.setFrameShape(QFrame.StyledPanel)
        self.usernameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.usernameFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.usernameInput_4 = QLineEdit(self.usernameFrame)
        self.usernameInput_4.setObjectName(u"usernameInput_4")
        sizePolicy.setHeightForWidth(self.usernameInput_4.sizePolicy().hasHeightForWidth())
        self.usernameInput_4.setSizePolicy(sizePolicy)
        self.usernameInput_4.setFont(font1)
        self.usernameInput_4.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")

        self.horizontalLayout_7.addWidget(self.usernameInput_4)


        self.horizontalLayout_8.addWidget(self.usernameFrame)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.passwordFrame = QFrame(self.frame_6)
        self.passwordFrame.setObjectName(u"passwordFrame")
        self.passwordFrame.setMinimumSize(QSize(250, 0))
        self.passwordFrame.setMaximumSize(QSize(16777215, 55))
        self.passwordFrame.setStyleSheet(u"Border: 1px solid rgba(255,255,255,30);\n"
"border-radius:10px;")
        self.passwordFrame.setFrameShape(QFrame.StyledPanel)
        self.passwordFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.passwordFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.passwordInput = QLineEdit(self.passwordFrame)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy)
        self.passwordInput.setFont(font1)
        self.passwordInput.setStyleSheet(u"background-color: #1c1a27;\n"
"Border: 0px;\n"
"")

        self.horizontalLayout_9.addWidget(self.passwordInput)


        self.horizontalLayout_10.addWidget(self.passwordFrame)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.registerButton = QPushButton(self.frame_3)
        self.registerButton.setObjectName(u"registerButton")
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setMaximumSize(QSize(250, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setKerning(True)
        self.registerButton.setFont(font2)
        self.registerButton.setStyleSheet(u"*{background-color: #18A558;\n"
"Border: 0px;\n"
"color: black;\n"
"Border-radius: 5px;\n"
"}\n"
"QPushButton:Hover{background-color: #56CC87}")

        self.horizontalLayout.addWidget(self.registerButton)

        self.errorLabel = QPushButton(self.frame_3)
        self.errorLabel.setObjectName(u"errorLabel")
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(9)
        self.errorLabel.setFont(font3)
        self.errorLabel.setStyleSheet(u"Border: 0px")

        self.horizontalLayout.addWidget(self.errorLabel)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Registration", None))
        self.pushButton_6.setText("")
        self.nameInput.setText("")
        self.nameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.usernameInput_4.setText("")
        self.usernameInput_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.errorLabel.setText("")
    # retranslateUi

