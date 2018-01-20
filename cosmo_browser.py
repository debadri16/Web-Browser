from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #progress bar
        self.pbar = QProgressBar()
        self.pbar.setMaximumWidth(120)

        #creating mainwindow page
        self.browser=QWebEngineView(loadProgress=self.pbar.setValue, loadFinished=self.pbar.hide,
                                  loadStarted=self.pbar.show, titleChanged=self.setWindowTitle)
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        #when mouse is hovered over any link
        self.browser.page().linkHovered.connect(self.if_link_hover)

        #creating statusbar
        self.browser.setMinimumSize(1200, 600)
        self.status = self.statusBar()
        self.status.addPermanentWidget(self.pbar)

        self.show()
        self.setWindowTitle("Cosmo")
        self.setWindowIcon(QIcon("cosmo.png"))

        #adding toolbar
        tb2 = QToolBar("Shortcuts")
        tb2.setIconSize(QSize(45,45))
        self.addToolBar(Qt.RightToolBarArea,tb2)

        #adding shortcut links of popular websites

        #creating each buttons
        wiki_btn = QAction(QIcon("wiki.png"), "Wikipedia", self)
        wiki_btn.setStatusTip("Go to Wikipedia - The Free Encyclopedia")
        wiki_btn.triggered.connect(lambda: self.conn("http://www.wikipedia.com"))
        tb2.addAction(wiki_btn)

        fb_btn = QAction(QIcon("facebook.png"), "Facebook", self)
        fb_btn.setStatusTip("Go to Facebook")
        fb_btn.triggered.connect(lambda:self.conn("http://www.facebook.com"))
        tb2.addAction(fb_btn)

        y_btn = QAction(QIcon("yahoo.png"), "Yahoo!", self)
        y_btn.setStatusTip("Go to Yahoo")
        y_btn.triggered.connect(lambda: self.conn("http://www.yahoo.com"))
        tb2.addAction(y_btn)

        tw_btn = QAction(QIcon("twitter.png"), "Twitter", self)
        tw_btn.setStatusTip("Go to Twitter")
        tw_btn.triggered.connect(lambda: self.conn("http://www.twitter.com"))
        tb2.addAction(tw_btn)

        red_btn = QAction(QIcon("reddit.png"), "Reddit", self)
        red_btn.setStatusTip("Go to Reddit")
        red_btn.triggered.connect(lambda: self.conn("https://reddit.com"))
        tb2.addAction(red_btn)

        ig_btn = QAction(QIcon("Instagram_icon.png"), "Instagram", self)
        ig_btn.setStatusTip("Go to Instagram")
        ig_btn.triggered.connect(lambda: self.conn("https://instagram.com"))
        tb2.addAction(ig_btn)

        li_btn = QAction(QIcon("linkedin.png"), "Linkedin", self)
        li_btn.setStatusTip("Go to Linkedin")
        li_btn.triggered.connect(lambda: self.conn("https://linkedin.com"))
        tb2.addAction(li_btn)

        git_btn = QAction(QIcon("github.png"), "Github", self)
        git_btn.setStatusTip("Go to Github")
        git_btn.triggered.connect(lambda: self.conn("https://github.com"))
        tb2.addAction(git_btn)

        stack_btn = QAction(QIcon("stack.png"), "Stack Overflow", self)
        stack_btn.setStatusTip("Go to Stack Overflow")
        stack_btn.triggered.connect(lambda: self.conn("https://stackoverflow.com"))
        tb2.addAction(stack_btn)

        q_btn = QAction(QIcon("quora.png"), "Quora", self)
        q_btn.setStatusTip("Go to Quora")
        q_btn.triggered.connect(lambda: self.conn("https://quora.com"))
        tb2.addAction(q_btn)

        p_btn = QAction(QIcon("pin.jpg"), "Pinterest", self)
        p_btn.setStatusTip("Go to Pinterest")
        p_btn.triggered.connect(lambda: self.conn("https://pinterest.com"))
        tb2.addAction(p_btn)

        fk_btn = QAction(QIcon("flipkart.png"), "Flipkart", self)
        fk_btn.setStatusTip("Go to Flipkart")
        fk_btn.triggered.connect(lambda: self.conn("https://flipkart.com"))
        tb2.addAction(fk_btn)

        am_btn = QAction(QIcon("amazon.png"), "Amazon", self)
        am_btn.setStatusTip("Go to Amazon")
        am_btn.triggered.connect(lambda: self.conn("https://amazon.com"))
        tb2.addAction(am_btn)

        eb_btn = QAction(QIcon("ebay.png"), "Ebay", self)
        eb_btn.setStatusTip("Go to Ebay")
        eb_btn.triggered.connect(lambda: self.conn("https://ebay.com"))
        tb2.addAction(eb_btn)

        mmt_btn = QAction(QIcon("mmt.png"), "Makemytrip", self)
        mmt_btn.setStatusTip("Go to Makemytrip")
        mmt_btn.triggered.connect(lambda: self.conn("http://www.makemytrip.com"))
        tb2.addAction(mmt_btn)

        nx_btn = QAction(QIcon("netflix.png"), "Netflix", self)
        nx_btn.setStatusTip("Go to Netflix")
        nx_btn.triggered.connect(lambda: self.conn("http://www.netflix.com"))
        tb2.addAction(nx_btn)

        ib_btn = QAction(QIcon("imdb.png"), "IMDb", self)
        ib_btn.setStatusTip("Go to IMDb")
        ib_btn.triggered.connect(lambda: self.conn("https://imdb.com"))
        tb2.addAction(ib_btn)

        msn_btn = QAction(QIcon("msn.png"), "MSN", self)
        msn_btn.setStatusTip("Go to MSN")
        msn_btn.triggered.connect(lambda: self.conn("https://msn.com"))
        tb2.addAction(msn_btn)

        #another toolbar
        tb=QToolBar("Navigation")
        tb.setIconSize(QSize(25,25))
        self.addToolBar(tb)

        win_btn = QAction(QIcon("newwin"), "New Window", self)
        win_btn.setStatusTip("Create a new window")
        win_btn.triggered.connect(self.new_win)
        tb.addAction(win_btn)

        tb.addSeparator()

        back_btn=QAction(QIcon("Button-Back-1-512.png"),"Back",self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        tb.addAction(back_btn)


        fwd_btn = QAction(QIcon("forward.png"), "Forward", self)
        fwd_btn.setStatusTip("Forward to next page")
        fwd_btn.triggered.connect(self.browser.forward)
        tb.addAction(fwd_btn)

        home_btn = QAction(QIcon("home.png"), "Home", self)
        home_btn.setStatusTip("Go to home page")
        home_btn.triggered.connect(self.gohome)
        tb.addAction(home_btn)

        rld_btn = QAction(QIcon("refresh"), "Reload", self)
        rld_btn.setStatusTip("Reload this page")
        rld_btn.triggered.connect(self.browser.reload)
        tb.addAction(rld_btn)

        #ading URL bar
        self.urlbar=QLineEdit()
        tb.addSeparator()
        self.urlbar.returnPressed.connect(self.navigate_page)
        tb.addWidget(self.urlbar)

        #action to perform when URL is changed
        self.browser.urlChanged.connect(self.update_url)

        stop_btn=QAction(QIcon("stop.png"),"Stop",self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        tb.addAction(stop_btn)

        self.statusBar().showMessage('Cosmo Browser')
        self.show()

    #to open another window
    def new_win(self):
        windo = MainWindow()
        windo.show()

    #edit URL bar
    def update_url(self,q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    #open home page
    def gohome(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    #user entered URL tasks
    def navigate_page(self):
        q=QUrl(self.urlbar.text())
        t=self.urlbar.text()
        if "." not in t:
            t='http://www.google.com/search?q='+t
            self.browser.setUrl(QUrl(t))
        elif q.scheme()=="":
            q.setScheme("http")
            self.browser.setUrl(q)
        else:
            self.browser.setUrl(q)

    #connect shortcut websites
    def conn(self,s):
        self.browser.setUrl(QUrl(s))

    #change status
    def if_link_hover(self, l):
        self.status.showMessage(l)

#usual
app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec())
