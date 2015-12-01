#!/usr/bin/env python2.7
#coding=utf-8

"""
Author:         charliezhao
Filename:       gridlayout.py
Create Time:  2015-12-01 19:32
Description:
                
"""
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

class GridLayout(QtGui.QWidget):
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setGeometry(300, 300, 350, 80)
        self.setWindowTitle('grid layout')

        names = ['Cls', 'Bck', 'Close', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

        grid = QtGui.QGridLayout()
        grid.setSpacing(20) 
        j = 0
        pos = [ (0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3),
                (4, 0), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:
                grid.addWidget(QtGui.QLabel('hello charliezhaoooooooooooooooooooooo'), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1
        
        edit = QtGui.QLineEdit()
        grid.addWidget(edit, 5, 0, 2, 0)

        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal,
                               self)
        
        self.connect(slider,
                     QtCore.SIGNAL('valueChanged(int)'),
                     lcd,
                     QtCore.SLOT('display(int)'))
        grid.addWidget(lcd, 8, 0, 10, 4)
        grid.addWidget(slider, 19, 0, 1, 4)
       

        tbutton = QtGui.QPushButton('button1')
        grid.addWidget(tbutton, 20, 0)
        self.connect(tbutton,
                     QtCore.SIGNAL('clicked()'),
                     self.showDialog)
       
        cbutton = QtGui.QPushButton('button2')
        grid.addWidget(cbutton, 20, 1)
        self.connect(cbutton,
                     QtCore.SIGNAL('clicked()'),
                     self.showDialog2)        
        
        fbutton = QtGui.QPushButton('button3')        
        grid.addWidget(fbutton, 20, 2)
        self.connect(fbutton,
                     QtCore.SIGNAL('clicked()'),
                     self.showDialog3)

        fbutton2 = QtGui.QPushButton('button4')
        grid.addWidget(fbutton2, 20, 3)
        self.connect(fbutton2,
                     QtCore.SIGNAL('clicked()'),
                    self.showDialog4)

        self.label = QtGui.QLabel('')
        grid.addWidget(self.label, 21, 0)
        
        self.textEdit = QtGui.QTextEdit()
        grid.addWidget(self.textEdit, 22, 0, 4, 4)

        self.cb = QtGui.QCheckBox("show title", self)
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb.toggle()
        self.connect(self.cb,
                     QtCore.SIGNAL('stateChanged(int)'),
                     self.changeTitle)
        grid.addWidget(self.cb, 27, 0)

        self.pbar = QtGui.QProgressBar(self)
        grid.addWidget(self.pbar, 28, 1, 1, 3)
        
        self.pbutton = QtGui.QPushButton('pbutton')
        grid.addWidget(self.pbutton, 27, 1)
        self.connect(self.pbutton, 
                     QtCore.SIGNAL('clicked()'),
                     self.onStart)
        


        self.setLayout(grid)
        self.step = 0
        self.timer = QtCore.QBasicTimer()
        # self.connect(self,
        #              QtCore.SIGNAL('closeEmitApp()'),
        #              QtCore.SLOT('close()'))        
    
    def timerEvent(self, event):
        if self.step >= 1000:
            self.timer.stop()
            return
        self.step += 1
        self.pbar.setValue(self.step)
    
    def onStart(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pbutton.setText('Start')
        else:
            self.timer.start(1000, self)
            self.pbutton.setText('Stop')

    def changeTitle(self, value):
        if self.cb.isChecked():
            # self.setWindowTitle('CheckBox')
            self.setWindowTitle(str(value))
        else:
            # self.setWindowTitle('unchecked')
            self.setWindowTitle(str(value))

    def showDialog4(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'open file', '~')
        with open(filename, 'r') as f:
            data = f.read()
            self.textEdit.setText(unicode(data, 'utf-8'))

    def showDialog3(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

    def showDialog2(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            print(col)

    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self,
                                              'input dialog',
                                              'enter your name:')
        if ok:
            self.label.setText(unicode(text))


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


app = QtGui.QApplication(sys.argv)
qb = GridLayout()
qb.show()
sys.exit(app.exec_())
