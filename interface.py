import qtawesome as qta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QThread, left, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QHBoxLayout,
                             QLabel, QMainWindow, QMenu, QMenuBar, QPushButton,
                             QVBoxLayout, QWidget)
import numpy as np 
import sys        
class App(QWidget):
   
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: lightgrey;")
        self.setWindowTitle("To Be Determine")
        self.disply_width = 1500
        self.display_height = 900
        self.crop_w = 240
        self.crop_h = 160
        self.IconSize = QSize(60, 60)
        self.setFixedSize(self.disply_width, self.display_height)
        hbox = QGridLayout()
        self.setLayout(hbox)
if __name__ == "__main__":
    def __init__(self):
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        # QMainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())