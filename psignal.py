#!/usr/bin/env python2.7
#coding=utf8

"""
Author:         charliezhao
Filename:       psignal.py
Create Time:  2015-11-21 10:39
Description:
                
"""
import sys
import signal

def timeout_handler(signum, frame):
    print("SIFALRM catch")
    sys.exit(0)


def quit_handler(signum, frame):
    print("SIGQUIT catch")
    sys.exit(0)


def int_handler(signum, frame):
    print("SIGINT catch")
    sys.exit(0)


def signal_default():
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.signal(signal.SIGQUIT, quit_handler)
    signal.signal(signal.SIGINT, int_handler)    
