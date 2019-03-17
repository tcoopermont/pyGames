#!/usr/bin/python3

from random import randrange
import curses
from curses import wrapper
import time

digList = []
validInput = ['1','2','3','4','5','6','7','8','9']
tryDigList = []


def genPuz(len):
  digList = []
  for i in range(len):
    digList.append(randrange(1,9))
  return digList


digList = genPuz(7)

#for i in digList:
#  print(i)


def dispPuz(stdscr):
  curses.curs_set(0) # make cursor invisible
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
  dispSleep = 1
  stdscr.clear()
  for i in range(5):
    stdscr.addstr(2,2*i,str(i))

  stdscr.refresh()
  #stdscr.addstr(2,2*i,str(i),curses.A_BLINK)
  for i in range(5):
    stdscr.addstr(2,2*i,str(i),curses.color_pair(1))
    stdscr.refresh()
    time.sleep(dispSleep)
    stdscr.addstr(2,2*i,str(i))
    stdscr.refresh()
    time.sleep(dispSleep)

  time.sleep(1)
  #stdscr.getkey()


def echoKey(stdscr):
  curses.curs_set(0) # make cursor invisible
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
  stdscr.clear()
  for i in range(5):
    stdscr.addstr(2,2*i,str(i))

  stdscr.refresh()
  dig = stdscr.getkey()
  while dig in validInput:
    i = int(dig)
    tryDigList.append(i)
    stdscr.addstr(2,2*i,str(i),curses.color_pair(1))
    stdscr.refresh()
    time.sleep(1)
    stdscr.addstr(2,2*i,str(i))
    stdscr.refresh()
    dig = stdscr.getkey()
  
wrapper(dispPuz)
wrapper(echoKey)
  
for i in tryDigList:
  print(i)
