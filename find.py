# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

MAC = "qt_mac_set_native_menubar" in dir()

class FindAndReplaceDlg(QDialog):
    def __init__(self, parent=None):
        super(FindAndReplaceDlg, self).__init__(parent)
        
        self.find_label = QLabel("find_label:")
        self.find_line_edit = QLineEdit("QLineEdit")
        self.find_label.setBuddy(self.find_line_edit)

        self.replace_label = QLabel("replace_label:")
        self.replace_line_edit = QLineEdit("QLineEdit")
        self.replace_label.setBuddy(self.replace_line_edit)
        
        self.case_check_box = QCheckBox("Case Sensitive")
        self.whole_check_box = QCheckBox("Whole words")
        self.whole_check_box.setChecked(True)
        
        self.backwords_check_box = QCheckBox("Search Backwords.")
        self.regex_check_box = QCheckBox("Regular Expression")
        self.ignore_notes_check_box = QCheckBox("Ignore footnotes and end points")
        
        self.more_frame = QFrame()
        self.more_frame.setFrameStyle(QFrame.VLine|QFrame.Sunken)
        self.more_frame.hide()
       
        self.find_button = QPushButton("find_button")
        self.replace_button = QPushButton("replace_button")
        self.close_button = QPushButton("close_button")
        self.more_button = QPushButton("more_button")
        self.more_button.setCheckable(True)
        
        self.custom_layout()
        self.custom_connect()
        
        self.setWindowTitle("hello by charlie zhao")
    
    def custom_connect(self):
        self.connect(self.more_button, SIGNAL("clicked(bool)"),
                     self.more_frame, SLOT("setVisible(bool)") )
        
    def custom_layout(self):
        """set all kinds of layout"""
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.find_label, 0, 0)
        grid_layout.addWidget(self.find_line_edit, 0, 1)
        grid_layout.addWidget(self.replace_label, 1, 0)
        grid_layout.addWidget(self.replace_line_edit, 1, 1)
        
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(self.case_check_box)
        frame_layout.addWidget(self.whole_check_box)
        
        more_frame_layout = QVBoxLayout()
        more_frame_layout.addWidget(self.backwords_check_box)
        more_frame_layout.addWidget(self.regex_check_box)
        more_frame_layout.addWidget(self.ignore_notes_check_box)
        self.more_frame.setLayout(more_frame_layout)
        
        left_layout = QVBoxLayout()
        left_layout.addLayout(grid_layout)
        left_layout.addLayout(frame_layout)
        left_layout.addWidget(self.more_frame)
        
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.find_button)
        button_layout.addWidget(self.replace_button)
        button_layout.addWidget(self.close_button)
        button_layout.addWidget(self.more_button)
        
        main_layout= QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(button_layout)
        main_layout.setSizeConstraint(QLayout.SetFixedSize)
         
        self.more_frame.setLayout(more_frame_layout)
        self.setLayout(main_layout)
        
if __name__ == "__main__":
    def find(what, *args):
        print "Find %s %s" % (what, [x for x in args])

    def replace(old, new, *args):
        print "Replace %s with %s %s" % (old, new, [x for x in args])

    app = QApplication(sys.argv)
    form = FindAndReplaceDlg()
    form.connect(form, SIGNAL("find"), find)
    form.connect(form, SIGNAL("replace"), replace)
    form.show()
    app.exec_()