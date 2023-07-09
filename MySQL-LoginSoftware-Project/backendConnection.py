##  Name: backendConnection
##  Copyright: © 2023 John0x44. All rights reserved.
##  Author: John0x44
##  Date: 21/06/23 18:10
##  Description: Connect main frontend and backend 

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from database import SQL
from functools import partial 

from otherWindows.backendConnection import CONNECT_REG_UI 


#DONE: quick implementation...
#DONE: contiously and asynchronously check database connection... implemented QTimer 

# Connecting backend to frontend 
class CONNECT_UI:
    def __init__(self, UI, REGISTER_UI):
        self.REGISTER_UI = REGISTER_UI
        self.UI = UI
        self.DBConnection = SQL()
        self.DBConnection.connectDB()
        self.loginState = self.UI.LoginState
        self.loginButton = self.UI.LoginButton
        self.registerButton = self.UI.RegisterButton
        self.userInput = self.UI.usernameInput
        self.passInput = self.UI.passwordInput 

        # Database checktime 
        self.checkTime = 5 

        self.timer = QTimer()
        self.timer.timeout.connect(self.checkDBStatus)
        self.timer.start(self.checkTime*1000)  

        # on initialization
        self.getDBStatus()
        CONNECT_REG_UI(REGISTER_UI, self.DBConnection)

        # Handle client buttons
        self.loginButton.clicked.connect(partial(self.updateLogin))
        self.registerButton.clicked.connect(partial(self.handleRegister))

        # Toggle highlight 
        self.userInput.textChanged.connect(partial(self.highlightInput,self.UI.usernameFrame))
        self.passInput.textChanged.connect(partial(self.highlightInput,self.UI.passwordFrame))
        
    # Get database status 
    def checkDBStatus(self):
        if not self.getDBStatus():
            self.updateLoginState("Error: Database offline", 255, 0, 0, 200)

    # Get database status 
    def getDBStatus(self) -> bool:
        DBStatus = not self.DBConnection.databaseError
        self.updateDBStatus(DBStatus)
        print(f"[Debug] Database status checked -> reported: {DBStatus}")
        return DBStatus
    
    # Update login 
    def updateLogin(self):
        inputUser = self.userInput.text()
        inputPass = self.passInput.text()
        if len(inputUser) > 0 and len(inputPass) > 0:
            userState = self.DBConnection.checkUsername(inputUser)
            if not self.getDBStatus():
                self.updateLoginState("Error: Database offline", 255, 0, 0, 200)
            else: 
                if userState:
                    loginState = self.DBConnection.userLogin(inputUser, inputPass)
                    if loginState:
                        self.updateLoginState("Successful login!", 0, 255, 0, 200)
                        self.updateWelcomeStatus(self.DBConnection.getName(inputUser))
                    else: 
                        self.updateLoginState("Login failed!", 255, 0, 0, 200)
                else:
                    self.updateLoginState("Please register", 255, 0, 0, 200)
        else:
            self.updateLoginState("Type your full credentials", 255, 0, 0, 200)

     # Update state
    def updateLoginState(self, text, r, g, b, t):
        self.loginState.setText(f"{text}")
        self.loginState.setStyleSheet(f"color: rgba({r}, {g}, {b}, {t})")
    
    # Update welcome status 
    def updateWelcomeStatus(self, name):
        self.UI.WelcomeLabel.setText(f"Welcome, {name}")

    # Update database status 
    def updateDBStatus(self, DBStatus):
        if DBStatus:
            self.UI.DatabaseLabel.setStyleSheet("color: green; border: 0px;")
        else:
            self.UI.DatabaseLabel.setStyleSheet("color: red; border: 0px;")
        self.UI.DatabaseLabel.setText(f"Database Connected: {DBStatus}")

    # Handle register
    def handleRegister(self):
        self.REGISTER_UI.MainWindow.show()

    # Handling highlight on client inputs 
    def highlightInput(self, widget, key):
        widget.setStyleSheet("border: 1px solid rgba(255, 255, 255, 200);border-radius: 10px;")
        if hasattr(widget, "typingTimer"):
            widget.typingTimer.stop()
        else:
            widget.typingTimer = QTimer()
            widget.typingTimer.setInterval(1000)  
            widget.typingTimer.setSingleShot(True)
            widget.typingTimer.timeout.connect(lambda: self.handleTypingTimeout(widget))
        widget.typingTimer.start()

    def handleTypingTimeout(self, widget):
        widget.setStyleSheet("border: 1px solid rgba(255, 255, 255, 20);border-radius: 10px;")
