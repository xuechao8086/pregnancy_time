#!/usr/bin/env python2.7
#-*-encoding:gbk*-
"""
Author:         charliezhao
Filename:       pregnancytime.py
Create Time:    2015-10-01 15:38
Description:
    pregnancy time.
ToDo:
    curses programming.
"""
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import os
import time
#import curses


__all__ = ["getpregancy_time"]


def display_info(std, x, y, colorpair=1):
    global stdscr
    stdscr.addstr(y, x, str, curses.color_pair(colorpair))
    stdscr.refresh()


def get_ch_and_continue():
    global stdscr
    stdscr.nodelay()
    ch = stdscr.getch()
    stdscr.nodelay(1)
    return True


def set_win():
    global stdscr
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1)


def unset_win():
    global stdscr
    curses.nocbreak()
    curses.echo()
    curses.endwin()

def create_new_win(begin_x, begin_y, width, height):
    global stdscr 
    stdscr.refresh()
    return cruses.newwin(height, width, begin_y, begin_x)


def pad():
    pad = curses.newpad(10, 10)
    for y in xrange(0, 10):
        for x in xrange(0, 10):
            try:
                pad.addch(y, x, ord('a')+(x*x+y*y)%26)
            except curses.error:
                print('error')
                pass
    pad.refresh(0, 0, 5, 5, 20, 75)
    return pad


def addstr():
    global stdscr 
    #stdscr.addstr(0, 0, "current mode: typing mode",
    #        curses.A_REVERSE)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr("pretty text", curses.color_pair(1))
    stdscr.refresh()


if __name__ == '__test__':
    stdscr = curses.initscr()
    pad() 
    addstr() 
    try:
        set_win()
        display_info("hola, curses!", 1, 1)
        display_info("charliezhao first test!", 100, 100)
        get_ch_and_continue()
    except Exception as e:
        print(e)
    finally:
        unset_win()


def getpregancy_time(begin, end):
    """
    `param begin`: str time
    `param end`: str time
    """
    begin_time_tuple = time.strptime(begin, "%Y-%m-%d %H:%M:%S")
    end_time_tuple = time.strptime(end, "%Y-%m-%d %H:%M:%S")
    
    beginstamp = time.mktime(begin_time_tuple)
    endstamp = time.mktime(end_time_tuple)
    
    days = (endstamp-beginstamp)//(24*3600)
    weeks = days//7
    days2 = days%7

    
    print(unicode("总共{}天（{}周零{}天， 小于 {}周整）".format(days, weeks, days2, weeks+1), "gbk"))


def timezone(zone):
    """set time zone"""
    os.environ['TZ'] = zone
    time.tzset()


if __name__ == "__main__":
    zone="GMT-8"
    # timezone(zone) 

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    fertilizationend_time = "2015-09-03 00:00:00"
    menstrual_time = "2015-08-19 00:00:00"
    implantation_time = "2015-09-06 00:00:00" 
    

    print(unicode("从 {} 到 {}:".format(menstrual_time, now), "gbk"))
    getpregancy_time(menstrual_time, now)
    print('')
    print('')
    print('')


    time.sleep(120)
