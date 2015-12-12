#!/usr/bin/env python2.7
#coding=utf-8

"""
Author:         charliezhao
Filename:       ptime_qt.py
Create Time:  2015-12-03 17:22
Description:

"""
import sys
import platform
import os
import time
import xlrd

from PyQt4 import QtCore 
from PyQt4 import QtGui 
from PyQt4 import QtNetwork 
from PyQt4 import QtWebKit

try:
    import jquery_rc3
except importError:
    import jquery_rc2

class MainWindow(QtGui.QMainWindow):
    def __init__(self, url):
        super(MainWindow, self).__init__()
        self.debug = False
        self.dat = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                                "./dat.xls") 
       
        self.beg = "2015-08-19 00:00:00"  
        self.now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        self.days, self.weeks, self.days2, self.month, self.valstr = self.get_pregnancy_time(self.beg,
                                                                                             self.now)

        QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True) 
        self.view = QtWebKit.QWebView(self)
        self.view.load(url)

        super(MainWindow, self).__init__()

        # calcGroupBox = QtGui.QGroupBox(u"预产期计算器")
        QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)        
        self.view = QtWebKit.QWebView(self)
        self.view.load(url)
        # self.view.setHtml("<html><body><b>not found</b>", QtCore.QUrl()) 
        
        # calcLayout = QtGui.QHBoxLayout()
        # calcLayout.addWidget(self.view)
        # calcGroupBox.setLayout(calcLayout)        

        self.searchEdit = QtGui.QLineEdit(self)
        self.searchEdit.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                      self.searchEdit.sizePolicy().verticalPolicy()) 
        self.searchEdit.returnPressed.connect(self.search)        
        
        choiceGroupBox = QtGui.QGroupBox(u"")
        self.radio1 = QtGui.QRadioButton(u"今日第{:>3d}天, 预产期计算器".format(self.days))
        self.radio2 = QtGui.QRadioButton(u"本周第{:>3d}周, 宝发育图解".format(self.weeks+1))
        self.radio3 = QtGui.QRadioButton(u"本周第{:>3d}周, excel提醒".format(self.weeks+1))
        self.radio4 = QtGui.QRadioButton(u"本月第{:>3d}月，产检项目和时间安排".format(self.month+1))
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radio1Click)
        self.radio2.clicked.connect(self.radio2Click)        
        self.radio3.clicked.connect(self.get_notice)        
        self.radio4.clicked.connect(self.radio4Click)        

        choiceLayout = QtGui.QVBoxLayout()
        choiceLayout.addWidget(self.radio1)
        choiceLayout.addWidget(self.radio4)
        choiceLayout.addWidget(self.radio3)
        choiceLayout.addWidget(self.radio2)
        choiceLayout.addStretch(1)
        choiceGroupBox.setLayout(choiceLayout)
        
        dateGroupBox = QtGui.QGroupBox(u"")
        self.calendar = QtGui.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(2015, 8, 19))        
        self.calendar.setMaximumDate(QtCore.QDate(2016, 6, 1))        
        self.calendar.setGridVisible(True)
        dateLayout = QtGui.QGridLayout()
        dateLayout.addWidget(self.calendar, 0, 0,
                               # QtCore.Qt.AlignCenter)
                               QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        dateGroupBox.setLayout(dateLayout)
      
        leftLayout = QtGui.QVBoxLayout()
        leftLayout.addWidget(choiceGroupBox) 
        leftLayout.addWidget(dateGroupBox)

        # dateMenu = self.menuBar().addMenu(u"&日期")
        # yesterdayAction = QtGui.QAction(u"昨日", self)
        # yesterdayAction.triggered.connect(self.yesterday)        
        # tomorrowAction = QtGui.QAction(u"明日", self)
        # tomorrowAction.triggered.connect(self.tomorrow) 
        # dateMenu.addAction(yesterdayAction)        
        # dateMenu.addAction(tomorrowAction)
        
        opMenu = self.menuBar().addMenu(u"&操作")
        radio1Action = QtGui.QAction(u"预产期计算器", self)
        radio2Action = QtGui.QAction(u"宝宝发育图解", self)
        radio3Action = QtGui.QAction(u"excel提醒", self)
        radio4Action = QtGui.QAction(u"产检项目和时间安排", self)        
        radio1Action.triggered.connect(self.radio1Click)        
        radio2Action.triggered.connect(self.radio2Click)        
        radio3Action.triggered.connect(self.get_notice)        
        radio4Action.triggered.connect(self.radio4Click)        
        opMenu.addAction(radio1Action)
        opMenu.addAction(radio2Action)
        opMenu.addAction(radio3Action)
        opMenu.addAction(radio4Action)

        
        aboutMenu = self.menuBar().addMenu(u"&关于")
        aboutAction = QtGui.QAction(u"关于", self)        
        aboutAction.triggered.connect(self.about)
        aboutMenu.addAction(aboutAction)

        toolBar = self.addToolBar(u"工具栏")
        # toolBar.addAction(yesterdayAction)        
        # toolBar.addAction(tomorrowAction)        
        toolBar.addWidget(self.searchEdit)        

        widget = QtGui.QWidget()
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addLayout(leftLayout) 
        mainLayout.addWidget(self.view) 
        widget.setLayout(mainLayout) 
        
        self.setCentralWidget(widget)
        
        self.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint)
        label = QtGui.QLabel("test for charlie")
        label.setGeometry(300, 300, 10, 10)

        self.setWindowTitle(u"婷婷怀孕工具箱")        

    def about(self):
        QtGui.QMessageBox.about(self, 
                                u"婷婷怀孕工具箱",
                                u'by charliezhao<br/>部分工具来自<a href=""http://www.berqin.com">倍儿亲育婴</a>')        

    def radio1Click(self):
        # print 'radio1 click'
        path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                            "ptime.html")

        url = QtCore.QUrl(path)
        self.view.load(url)        

    def radio2Click(self):
        # print 'radio2 click'
        url = QtCore.QUrl("http://www.berqin.com/app/fayuguocheng/2-0-0-{}.html".format(self.weeks))
        self.view.load(url)        
        
    def radio4Click(self):
        path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                            "pnotice.html")
        
        url = QtCore.QUrl(path) 
        self.view.load(url)        

    def finishLoading(self):
        pass

    def search(self):
        print(self.searchEdit.text())        

    def yesterday(self):
        pass

    def tomorrow(self):
        pass
   
    
    def get_pregnancy_time(self, beg, end):
        """
        `param beg`: %Y-%m-%d %H:%M:%S
        `param end`: %Y-%m-%d %H:%M:%S
        """
        beg_tuple = time.strptime(beg, "%Y-%m-%d %H:%M:%S")        
        end_tuple = time.strptime(end, "%Y-%m-%d %H:%M:%S")        
          
        begsc = time.mktime(beg_tuple)
        endsc = time.mktime(end_tuple)
        
        days = int((endsc-begsc)//(24*3600))
        weeks = int(days//7)
        days2 = int(days%7)
        month = int(days//28) 
        val = u"{}天".format(days) 
        return (days, weeks, days2, month, val)
   
    def chk_unix(self):    
        """return wether on win""" 
        pf =  platform.system().lower()        
        if pf.find('win') != -1:
            return False 
        else:
            return True
    
    def set_zone(self):
        """only on UNIX"""
        zone = "GMT-8"        
        if self.chk_unix():
            os.environ['TZ'] = zone
            time.tzset()
    
    def get_notice(self):
        """""" 
        content = """<p><span style="color:red;">今日第{}天({}周+{}天):</span><br/>{} </p>
                     <p><span style="color:red;">本周第{}周:</span><br/>{}</p>
                     <p><span style="color:red;">本月第{}月:</span><br/>{}</p>""".format(self.days, self.weeks, self.days2, self.get_daily(self.days+1, 4),
                                                         self.weeks+1, self.get_week(self.weeks+3, 3),
                                                         self.month+1, self.get_month(2+(self.month)*4, 13))
    
        self.view.setHtml(content.decode('utf-8'), QtCore.QUrl())


    def get_daily(self, row, col):
        """return utf-8 str from excel"""
        with xlrd.open_workbook(self.dat) as book:
            sh = book.sheet_by_index(0)
            if self.debug:    
                print "Worksheet name(s): ",book.sheet_names()[0]
                print 'book.nsheets',book.nsheets
                print 'sh.name:',sh.name,'sh.nrows:',sh.nrows,'sh.ncols:',sh.ncols
            try: 
                return sh.cell_value(row, col).encode('utf-8') 
            except:
                return u"无内容可显示，请检查excel".encode('utf-8')
    
    def get_week(self, row, col):
        with xlrd.open_workbook(self.dat) as book:
            sh = book.sheet_by_index(1)
            if self.debug:
                print "Worksheet name(s): ",book.sheet_names()[1]
                print 'book.nsheets',book.nsheets 
                print 'sh.name:',sh.name,'sh.nrows:',sh.nrows,'sh.ncols:',sh.ncols
            try:
                return sh.cell_value(row, col).encode('utf-8') 
            except:
                return u"无内容可显示, 请检查excel".encode('utf-8')
        
    def get_month(self, row, col):
        # print("row={}, col={}".format(row, col))
        with xlrd.open_workbook(self.dat) as book:
            sh = book.sheet_by_index(4)
            if self.debug:
                print "Worksheet name(s): ",book.sheet_names()[4]
                print 'book.nsheets',book.nsheets
                print 'sh.name:',sh.name,'sh.nrows:',sh.nrows,'sh.ncols:',sh.ncols
                for i in xrange(2,sh.nrows):
                    for j in xrange(2, sh.ncols):
                        try:
                            print i, j, sh.cell_value(i, j).encode('utf-8')
                        except:
                            print i, j, 'no val'
                
            try:
                nutrient = sh.cell_value(row, col-2).encode('utf-8')            
                role = sh.cell_value(row, col-1).encode('utf-8')
                note = sh.cell_value(row, col).encode('utf-8')

                return "营养素:{}<br/>作用:{}<br/>说明:{}<br/>".format(nutrient, role, note)
            except:
                return u"无内容可显示，请检查excel".encode('utf-8')

   

if __name__ == '__main__': 
    app = QtGui.QApplication(sys.argv)
    iconpath = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                            "images",
                            "icon.png"
                           )    
    app.setWindowIcon(QtGui.QIcon(iconpath))

    if len(sys.argv) > 1:
        url = QtCore.QUrl(sys.argv[1])
    else:
        path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "ptime.html")
        # url = QtCore.QUrl("http://www.baidu.com") 
        # url = QtCore.QUrl("http://www.berqin.com/app2/ycqjsq/")
        url = QtCore.QUrl(path)            
        # url = QtCore.QUrl("http://www.berqin.com/app/fayuguocheng/2-0-0-2.html")

    browser = MainWindow(url) 
    # browser.show() 
    # browser.showFullScreen() 
    browser.showMaximized() 
    sys.exit(app.exec_())
