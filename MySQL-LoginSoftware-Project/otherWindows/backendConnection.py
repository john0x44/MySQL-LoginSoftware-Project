##  Name: backendConnection
##  Copyright: © 2023 John0x44. All rights reserved.
##  Author: John0x44
##  Date: 21/06/23 18:10
##  Description: Connect frontend and backend for 'RegisterUI.py'

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functools import partial 

class CONNECT_REG_UI:
    def __init__(self, UI, DB):
        self.UI = UI 
        self.DB = DB 

        # handle some inputs
        self.userNameInput = self.UI.usernameInput_4
        self.passInput = self.UI.passwordInput 
        self.nameInput = self.UI.nameInput 
        self.registerButton = self.UI.registerButton 
        self.registerStatus = self.UI.errorLabel 

        self.registerButton.clicked.connect(partial(self.handleRegister))

    # Handle client register 
    def handleRegister(self):
        userName = self.userNameInput.text() 
        passWord = self.passInput.text() 
        name = self.nameInput.text() 
        if len(userName) > 0 and len(passWord) > 0 and len(passWord) > 0: 
            userStatus = self.DB.checkUsername(userName)
            if not(userStatus):
                # Register the user to database 
                self.DB.registerUser(name, userName, passWord)
                self.updateRegisterState("Successfully registered please login now!", 0,255,0,200)
            else:
                self.updateRegisterState("Username is taken!",255,0,0,200)
        else: 
            self.updateRegisterState("Please complete ALL fields!", 255,0,0,200)
    
    # Update register status 
    def updateRegisterState(self, text, r,g,b,t):
        self.registerStatus.setText(f"{text}")
        self.registerStatus.setStyleSheet(f"color: rgba({r},{g},{b},{t}); Border: 0px")