from PyQt5 import QtCore, QtGui, QtWidgets
from light.tabUiLight import Ui_tabWidget

class Tab(QtWidgets.QWidget, Ui_tabWidget):
    clicked = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        super(Tab, self).__init__(parent = parent)
        self.setupUi(self)

    def setActive(self, act):
        if act == 0:
            self.tabWidget_2.setStyleSheet("QWidget{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(25, 25, 25);\n"
"    padding:2px;\n"
"}QWidget:hover{\n"
"    background-color:rgb(201, 201, 201);\n"
"}")
        else:
            self.tabWidget_2.setStyleSheet("QWidget{\n"
"    background-color:rgb(170, 170, 170);\n"
"    color:rgb(35, 34, 39;\n"
"    padding:2px;\n"
"}")

    def setId(self, bId):
        self.tabPushButton.setObjectName(str(bId))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(int(self.tabPushButton.objectName()))
