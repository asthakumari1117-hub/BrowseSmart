import sys

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.wolframalpha.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # self.browser.page().profile().downloadRequested.connect(self.on_download_requested)
        #
        # def on_download_requested(self, download: QWebEngineDownloadItem):
        #     download.setPath('C:\Users\ayush\PycharmProjects\ChiBrowser\icons++')  # Set the desired file path to save the downloaded file
        #     download.accept()

        navbar = QToolBar()
        self.addToolBar(navbar)

        code_explain = QAction('CODE EXPLAINER', self)
        code_explain.triggered.connect(self.explainer)
        code_explain.setIcon(QIcon('icons++/code.png'))
        navbar.addAction(code_explain)

        word_pdf = QAction('WORD 2 PDF', self)
        word_pdf.triggered.connect(self.open_converter)
        word_pdf.setIcon(QIcon('icons++/change.png'))
        navbar.addAction(word_pdf)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setIcon(QIcon('icons++/back.png'))
        navbar.addAction(back_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        home_btn.setIcon(QIcon('icons++/home.png'))
        navbar.addAction(home_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        forward_btn.setIcon(QIcon('icons++/forward.png'))
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setIcon(QIcon('icons++/reload.png'))
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.wolframalpha.com/'))

    def open_converter(self):
        self.browser.setUrl(QUrl('https://www.ilovepdf.com/word_to_pdf'))

    def explainer(self):
        self.browser.setUrl(QUrl('https://denigma.app/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('BrowseSmart')
window = MainWindow()
app.exec_()
