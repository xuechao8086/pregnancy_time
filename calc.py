#!/usr/bin/env python2.7
#coding=utf8

"""
Author:         charliezhao
Filename:       calc.py
Create Time:  2015-11-21 11:54
Description:
                
"""
from Tkinter import *


def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Simple Calculator")
        self.master.iconname("calcl")
        
        display = StringVar()
        Entry(self, relief=SUNKEN,
              textvariable=display).pack(side=TOP,
                                         expand=YES,
                                         fill=BOTH)
        
        for key in ("123", "456", "789", "0"):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, 
                       LEFT, 
                       char,
                       lambda w=display, s='%s'% char:w.set(w.get()+s))
    
        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                #btn.bind('<RuttonRelease-1>',
                #         lambda e, s=self,w=display:s.calc(w), '+')

        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr',
               lambda w=display:w.set(''))

if __name__ == '__main__':
    Calculator().mainloop()
