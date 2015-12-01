#!/usr/bin/python

# statusbar.py 

import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # self.resize(250, 150)
        self.setWindowTitle('statusbar')

        self.statusBar().showMessage('Ready')
        

        exit = QtGui.QAction(QtGui.QIcon('/Users/charlie/Pictures/http_www.apta.com.cn_Officer_PrintAdm.png'),
                             'Exit',
                             self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application') 
        exit.connect(exit,
                     QtCore.SIGNAL('triggered()'),
                     QtGui.qApp,
                     QtCore.SLOT("quit()")) 

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
    

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit)
        
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
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
