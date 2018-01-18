from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        self.show()
        self.setWindowTitle("Cosmo")
        self.setWindowIcon(QIcon("E:\pycharm\webbrowser\cosmo"))

        tb2 = QToolBar("Windows")
        tb2.setIconSize(QSize(15,15))
        self.addToolBar(Qt.LeftToolBarArea,tb2)
        tb2.setFixedSize(25,40)

        tab_btn = QAction(QIcon("E:\pycharm\webbrowser\window.png"), "New Window", self)
        tab_btn.setStatusTip("Open new window")
        tab_btn.triggered.connect(self.new_win)
        tb2.addAction(tab_btn)

        tb=QToolBar("Navigation")
        tb.setIconSize(QSize(25,25))
        self.addToolBar(tb)

        back_btn=QAction(QIcon("E:\pycharm\webbrowser\Button-Back-1-512.png"),"Back",self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        tb.addAction(back_btn)

        fwd_btn = QAction(QIcon("forward.png"), "Forward", self)
        fwd_btn.setStatusTip("forward to next page")
        fwd_btn.triggered.connect(self.browser.forward)
        tb.addAction(fwd_btn)

        home_btn = QAction(QIcon("E:\pycharm\webbrowser\download.png"), "Home", self)
        home_btn.setStatusTip("Go to home page")
        home_btn.triggered.connect(self.gohome)
        tb.addAction(home_btn)

        rld_btn = QAction(QIcon("E:\pycharm\webbrowser\Graphicloads-100-Flat-Reload.ico"), "Reload", self)
        rld_btn.setStatusTip("Reload this page")
        rld_btn.triggered.connect(self.browser.reload)
        tb.addAction(rld_btn)

        self.urlbar=QLineEdit()
        tb.addSeparator()
        self.urlbar.returnPressed.connect(self.navigate_page)
        tb.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.update_url)

        stop_btn=QAction(QIcon("E:\pycharm\webbrowser\stop.png"),"Stop",self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        tb.addAction(stop_btn)

    def update_url(self,q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def gohome(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_page(self):
        q=QUrl(self.urlbar.text())
        if q.scheme()=="":
            q.setScheme("http")
        self.browser.setUrl(q)

    def new_win(self):
        pass


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()
