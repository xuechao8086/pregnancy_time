#!/usr/bin/env python2.7
#coding=utf-8

"""
Author:         charliezhao
Filename:       qt2.py
Create Time:  2015-12-01 18:17
Description:
                
"""
import sys
from PyQt4 import QtGui
app = QtGui.QApplication(sys.argv) 
widget = QtGui.QWidget() 
# widget.resize(250, 150) 
widget.resize(2500, 1500) 
widget.setWindowTitle('simple') 
widget.show() 
sys.exit(app.exec_())
