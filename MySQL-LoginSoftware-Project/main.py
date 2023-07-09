##  Name: main
##  Copyright: © 2023 John0x44. All rights reserved.
##  Author: John0x44
##  Date: 21/06/23 18:10
##  Description: Run the software application

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets

from backendUI import Ui_MainWindow
import sys 


from backendConnection import CONNECT_UI 
from otherWindows.RegisterUI import RegisterUI

class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #ADD REGISTER UI WINDOW
        self.REGISTER_UI_WINDOW=QtWidgets.QMainWindow() 
        self.REGISTER_UI=RegisterUI()
        self.REGISTER_UI.setupUi(self.REGISTER_UI_WINDOW)

        # Might need REGISTER_UI later...
        CONNECT_UI(self.ui, self.REGISTER_UI) 
        
        self.setWindowTitle("LoginDashboard")

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())