from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PyQt5.QtWidgets import *
from assets.webPageUi import Ui_wpWidget
import assets.data as data



class WebPage(QtWidgets.QWidget, Ui_wpWidget):
    def __init__(self, parent = None):
        super(WebPage, self).__init__(parent = parent)
        self.setupUi(self)

        self.webEngineView = QWebEngineView()
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_3.addWidget(self.webEngineView)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.page().profile().downloadRequested.connect(
            self.on_downloadRequested
        )
        url = "https://ww.webin.tilda.ws"
        self.view.load(QtCore.QUrl(url))
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)

        self.wpLineEdit.returnPressed.connect(self.load)
        self.wpPushButton.clicked.connect(self.backward)
        self.wpPushButton_2.clicked.connect(self.forward)
        self.wpPushButton_3.clicked.connect(self.reload)
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.settings)
        self.cheek()

    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self, download):
        old_path = download.url().path()  # download.path()
        suffix = QtCore.QFileInfo(old_path).suffix()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", old_path, "*." + suffix
        )
        if path:
            download.setPath(path)
            download.accept()

    def cheek(self):
        if data.fristlook == False:
            dlg = QMessageBox(self)

            try:
                look = open('assets/data.py', 'w')
                look.write('fristlook = True')
            except FileNotFoundError as e:
                print('Ошибка Сохронения Состояния Webin FristLook', e)

            data.fristlook = True

            dlg.setWindowTitle("Добро Пожаловать В Webin!")
            dlg.setText("Это Новый Webin теперь он как Chrome! \n\nЕсли у вас будут проблемы с значками кнопок\nУстановите в Папке DW Шрифт dripicons-v2.ttf\n\n Приятного Просмотра!")
            button = dlg.exec()
        else:
            print('Core Are Normal')
    def load(self):
        ex = False
        if ex == True:
            url = QtCore.QUrl.fromUserInput(self.wpLineEdit.text())
            self.wpLineEdit.setText(url.toString())
        else:
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
        self.webEngineView.load(QtCore.QUrl('https://duckduckgo.com/'))
    def settings(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("О Программе Webin")
        dlg.setText("Версия 23H2 Новая                                                               .\nДвижок PyQt5 \nСделанно NLive\n\nЕсли у вас проблемы с значками кнопок\nУстановите в Папке DW Шрифт dripicons-v2.ttf \n\nСайт Проекта ww.Webin.tilda.ws")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("Диалог Закрыт")

