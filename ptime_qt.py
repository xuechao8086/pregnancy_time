#!/usr/bin/env python2.7
#coding=utf-8

"""
Author:         charliezhao
Filename:       ptime_qt.py
Create Time:  2015-12-03 17:22
Description:

"""
import sys

from PyQt4 import QtCore, QtGui, QtNetwork, QtWebKit

class MainWindow(QtGui.QMainWindow):
    def __init__(self, url):
        super(MainWindow, self).__init__()
        
        self.searchEdit = QtGui.QLineEdit(self)
        self.searchEdit.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                      self.searchEdit.sizePolicy().verticalPolicy()) 
        self.searchEdit.returnPressed.connect(self.search)        
        
        self.choiceGroupBox = QtGui.QGroupBox("Choice") 
        self.calendar = QtGui.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(2015, 8, 19))        
        self.calendar.setMaximumDate(QtCore.QDate(2016, 6, 1))        
        self.calendar.setGridVisible(True)
        self.choiceLayout = QtGui.QGridLayout()
        self.choiceLayout.addWidget(self.calendar, 0, 0,
                                    QtCore.Qt.AlignCenter)
        self.choiceGroupBox.setLayout(self.choiceLayout)

        dateMenu = self.menuBar().addMenu(u"&日期")
        yesterdayAction = QtGui.QAction(u"昨日", self)
        yesterdayAction.triggered.connect(self.yesterday)        
        tomorrowAction = QtGui.QAction(u"明日", self)
        tomorrowAction.triggered.connect(self.tomorrow) 
        dateMenu.addAction(yesterdayAction)        
        dateMenu.addAction(tomorrowAction)
        
        toolBar = self.addToolBar("toolBar")
        toolBar.addAction(yesterdayAction)        
        toolBar.addAction(tomorrowAction)        
        toolBar.addWidget(self.searchEdit)        
        
        self.mainLayout = QtGui.QGridLayout()
        self.setLayout(self.mainLayout)
        self.setWindowTitle(u"婷婷怀孕周期")        

    def search(self):
        print(self.searchEdit.text())        

    def yesterday(self):
        pass

    def tomorrow(self):
        pass

if __name__ == '__main__': 
    import sys 
    app = QtGui.QApplication(sys.argv)
    if len(sys.argv) > 1:
        url = QtCore.QUrl(sys.argv[1])
    else:
        url = QtCore.QUrl('http://www.google.com/ncr') 
    
    browser = MainWindow(url) 
    browser.show() 
    sys.exit(app.exec_())
