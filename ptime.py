#!/usr/bin/env python
#coding=utf-8
"""
Author:         charliezhao
Filename:       ptime.py
Create Time:  2015-11-21 11:05
Description:
ToDo:   
    unicode problem(fixed)
    find out what anchor mean?
"""
import functools
import os
import sys
import xlrd
import time
import platform
import sys 
import threading

from Tkinter import *

class Application(Frame):

    def __init__(self, master=None, debug=False):
        self.debug = debug 
        self.dat = os.path.join(os.path.dirname(sys.argv[0]),
                                "./dat.xls") 
        
        self.beg = "2015-08-19 00:00:00"
        self.end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())        
        self.now = time.mktime(time.localtime())
        
        master.title(sys.argv[0])
        master.option_add('*font', ('verdana', 13, 'bold')) 
        # master.geometry("300x200")
        
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
                


    def __del__(self):
        print 'del call'
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
                return u"无内容可显示，请检查excel"
    
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
                return u"无内容可显示, 请检查excel"
        
    def get_month(self, row, col):
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
                nutrient = sh.cell_value(row, col-2)            
                role = sh.cell_value(row, col-1) 
                note = sh.cell_value(row, col)

                return u"营养素:{}\n作用:{}\n说明:{}\n".format(nutrient, role, note)
            except:
                return u"无内容可显示，请检查excel"


    def createWidgets(self):

        days, weeks, days2, month, tval = self.get_pregnancy_time(
            '2015-08-19 00:00:00',
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            )

        #top bar
        self.topF = Frame(root, relief='raised', bd=1)
        self.topF.pack(side=TOP, fill=X, expand=NO)
        
        top_leftF = Frame(self.topF)
        top_leftF.pack(side=LEFT)
        top_rightF = Frame(self.topF)
        top_rightF.pack(side=RIGHT)

        self.time_label = StringVar()
        self.time_label.set(u"{}".format(
            time.strftime(u"%Y-%m-%d %H:%M:%S", time.localtime())))
    
        Label(top_leftF,
              textvariable=self.time_label).pack(side=TOP, padx=10, anchor=W)

        Button(top_rightF, 
               text=u"昨天", 
               relief=GROOVE,
               borderwidth=5,
               command=functools.partial(self.bupdate, 
                                         self.beg, 
                                         -1)).pack(side=LEFT,padx=5)
        
        Button(top_rightF,
               text=u"明天",
               relief=GROOVE,
               borderwidth=5,
               command=functools.partial(self.bupdate,
                                         self.beg,
                                         1)).pack(side=LEFT) 
        
        self.top_entry = StringVar()
        self.top_entry.set('')       
        Entry(top_rightF, textvariable=self.top_entry, width=100).pack(side=LEFT, fill=X)
        
        Button(top_rightF,
               text=u'rset',
               command=functools.partial(self.update_content,
                                         self.beg,
                                         self.end)).pack(side=LEFT)

        self.contentF = Frame(root)
        self.contentF.pack(side=TOP)        
        
        self.content_fill(self.beg,
                          self.end)

        # self.bottomF = Frame(root, width=100)
        # self.bottomF.pack(side=TOP)
        # self.bottom_label = StringVar()
        # self.bottom_label.set(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        
        # bottomLabelF = Frame(self.bottomF)
        # bottomLabelF.pack(side=RIGHT)
        # l = Label(bottomLabelF,
        #      textvariable=self.bottom_label)
        # l.pack(side=RIGHT, fill=X)
        # l.grid(row=1, column=99) 
        # l.place(in_=bottomLabelF,x=1, y=1, relx=0, rely=0, anchor=SE) 

        # bg_thread = threading.Thread(target=self.update_content, args=(self.beg, self.end))       
        # bg_thread.start()
        
        bg_thread = threading.Thread(target=self.update_time)
        bg_thread.start()
    
    def update_time(self):
        while True:
            self.time_label.set(time.strftime("%Y-%m:%d %H:%M:%S", time.localtime()))
            time.sleep(1)

    def bupdate(self, beg, days):
        self.now += days*24*3600
        end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.now))        
        
        try:
            self.update_content(beg, end)        
        except:
            assert False 

    def hello(self):
        print 'hello'

    def update_content(self, beg, end):
        self.contentF.destroy()
        self.contentF = Frame(root)
        self.contentF.pack(side=LEFT)        
        self.content_fill(beg, end)        

    def content_fill(self, beg, end):
        """
        `param beg`: begin time, format: %Y-%m-%d %H:%M:%S
        `param end`: end time, format: %Y-%m-%d %H:%M:%S
        """
        contentFT = Frame(self.contentF)        
        contentFT.pack(side=TOP)
        
        self.content_label = StringVar()
        self.content_label.set(u"从{}到{}".format(beg[:10], end[:10]))        
        Label(contentFT, textvariable=self.content_label).pack(side=TOP) 
        
        contentFL = Frame(self.contentF)
        contentFL.pack(side=TOP)
        days, weeks, days2, month, tval = self.get_pregnancy_time(beg, 
                                                                  end)

        #left side, daily note.
        dailyF = Frame(contentFL,
                       #relief=SUNKEN, bd=1
                      )
        dailyF.pack(side=LEFT)
        self.fill_text(dailyF,
                       lval=u"第{}天({}周另加{}天),日提醒:".format(days, weeks, days2),
                       cval=self.get_daily(days+1, 4)) 
        # notescroll.pack(side=RIGHT, fill=Y)
        # destroy method
        # dailyF.destroy()        
        
        # week
        weekF = Frame(contentFL)
        weekF.pack(side=LEFT)
        self.fill_text(weekF,
                       lval=u"第{}周,周提醒:".format(weeks+1),
                       cval=self.get_week(weeks+3, 3))
         
        # month
        monthF = Frame(contentFL)
        monthF.pack(side=LEFT)        
        self.fill_text(monthF,
                       lval=u"第{}月, 月提示:".format(month+1),
                       cval=self.get_month(2+(month)*4, 13))

    def fill_text(self, frame, lval, cval):
        """
        `param frame`: frame
        `param lval`: label value, utf8 str
        `param cval`: content value, utf8 str
        """

        # notelabel = Label(frame, text=lval,
        #                   justify=LEFT)
        # notelabel.grid(row=0, column=0, padx=5)        
        # notelabel.pack(side=TOP) 

        # notetext = Text(frame, height=50, width=50)
        notetext = Text(frame, width=50)
        notetext.tag_configure('big',
                               foreground='red',
                               font=('Verdana', 24, 'bold')) 
        notetext.tag_configure('mid', 
                               font=('Tempus Sans ITC', 20))
        notetext.tag_configure('groove',
                               relief=GROOVE,
                               borderwidth=2) 
        
        notetext.insert(INSERT, lval+u'\n', 'big') 
        notescroll = Scrollbar(frame, command=notetext.yview)
        notetext.configure(yscrollcommand=notescroll.set) 

        notetext.insert(END, cval, 'mid') 
        
        # ok, delete method, clear all text
        # notetext.delete(0.0, END)

        # notetext.grid(row=1, column=0)
        # notescroll.grid(row=1, column=1)
        notetext.pack(side=LEFT)        
        notescroll.pack(side=RIGHT, fill=Y)

    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets_discard(self):
        self.label = Label(root, 
                           text="Hello, Tkinter, from charliezhao",
                           fg = "red",
                           # width=30,
                           # height=2,
                           # wraplength=100,
                           # justify='left',
                           # anchor='n', # need to find out meaning
                           # font='{courier 20 bold}', # need to find out meaning
                           # bitmap='error' 
                          )

        self.label.pack()        
        
        self.text = Text(root)
        self.text.tag_config('a',
                             foreground='red', 
                            )
        self.text.insert(1.0, "first line\n")
        self.text.insert(INSERT, "second line\n")
        self.text.insert(INSERT, "third line\n")
        self.text.insert(END, "last line\n", ('a'))
        self.text.pack()        

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
    
        
        self.menubar = Menu(self)
        for item in ['python', 'java', 'c/c__']:
            self.menubar.add_command(label=item, command=self.hello_command)
        
        root['menu'] = self.menubar

    
    def hello_command(self):
        print "hello_command"

if __name__ == '__main__':

    root = Tk()
    app = Application(master=root)

    app.mainloop()
    root.destroy()
