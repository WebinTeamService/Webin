from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtWidgets import *
from light.webPageUiLight import Ui_wpWidget

class WebPage(QtWidgets.QWidget, Ui_wpWidget):
    def __init__(self, parent = None):
        super(WebPage, self).__init__(parent = parent)
        self.setupUi(self)

        self.webEngineView = QWebEngineView()
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(183, 183, 183))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_3.addWidget(self.webEngineView)

        self.wpLineEdit.returnPressed.connect(self.load)
        self.wpPushButton.clicked.connect(self.backward)
        self.wpPushButton_2.clicked.connect(self.forward)
        self.wpPushButton_3.clicked.connect(self.reload)
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.settings)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.wpLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)
            print(url)
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)
    def home(self):
        self.webEngineView.load(QtCore.QUrl('http://google.com'))
    def settings(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Версия Webin")
        dlg.setText("Webin Beta \nВерсия Modern Light 23H2                                                                .\nДвижок PyQt5 \nСделанно NLive \n\nWebinbr.tilda.ws                          ")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("Диалог Закрыт")

