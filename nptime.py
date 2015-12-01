#!/usr/bin/env python2.7
#coding=utf-8

"""
Author:         charliezhao
Filename:       nptime.py
Create Time:  2015-12-01 10:20
Description:
                
"""
import time
from Tkinter import *


class Application(Frame):
    def __init__(self, master=None, debug=False):
        master['width'] = master.winfo_screenwidth()
        master['height'] = master.winfo_screenheight()

        Frame.__init__(self, master)
        
        self.master = master
        self.debug = debug
        
        self.create_widgets()
        
    def create_widgets(self):    
        top_frame = Frame(self.master,
                          width=self.master.winfo_screenwidth())
        top_frame.grid(row=0, column=0)
        
        top_lframe = Frame(top_frame)
        top_lframe.grid(row=0, column=0)        
        top_rframe = Frame(top_frame)        
        top_rframe.grid(row=0, column=1)        
    
        self.time_string = StringVar()
        self.time_string.set(u"{}".format(
            time.strftime(u"%Y-%m-%d %H:%M:%S", time.localtime())))
        
        l = Label(top_lframe, textvariable=self.time_string)
        l.grid(row=0,
               column=0,
               # padx='1c'
               padx = 1)
        b1 = Button(top_lframe,
               text=u"昨天",)
        b1.grid(row=0,
                column=1,
                padx=5)        
        b2 = Button(top_lframe,
               text=u"明天")
        b2.grid(row=0,
                column=2,
                padx=5)
        
        self.entry_string = StringVar()
        e = Entry(top_lframe,
                  textvariable=self.entry_string,
                  width=100)
        e.grid(row=0,
               column=3)
        
        w = Canvas(top_rframe)
        w.grid(row=0,
               column=0)

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
