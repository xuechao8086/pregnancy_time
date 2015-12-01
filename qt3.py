#!/usr/bin/python
#coding=utf-8
# icon.py
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

class Icon(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150) 
        self.setWindowTitle('Icon by charlie') 
        # self.setWindowIcon(QtGui.QIcon('/Users/charlie/Pictures/http_www.apta.com.cn_Officer_PrintAdm.png'))
        self.setToolTip('This is a <b>QWidget</b> widget') 
        self.setToolTip("this is a <b>QWidget</b> widget") 
        
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))
        
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 60, 35)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, 
                     QtCore.SLOT('quit()'))
        
        self.center()
        
        ok = QtGui.QPushButton('OK')
        cancel = QtGui.QPushButton("Cancel")
       

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)        
    
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)        

        self.setLayout(vbox)
        self.resize(300, 150)


    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           u"你确定要推出吗？",
                                           QtGui.QMessageBox.Yes,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)


app = QtGui.QApplication(sys.argv) 
icon = Icon()
icon.show()
sys.exit(app.exec_())
