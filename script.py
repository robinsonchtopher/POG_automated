from turtle import down
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
#from main menu, navigate to the exhibition, pick both teams, move to middle(no team selected to control) and start game, after game get score?, update the bracket, find next game to sim
#bracketHQ

time.sleep(2)#delayed start to tab into the game

def click(x,y):
    win32api.SetCursePose((x,y))# move mouse to position x, y
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)#press down on left mouse button
    time.sleep(0.1)#holds for .1 sec
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

click(200,500) #would move the mouse to position 200,500 then click for .1 sec

#this would press the 1 key for .1 sec
pyautogui.keyDown('1')
time.sleep(0.1)
pyautogui.keyUp('1')
#wait to make sure game loads properly
time.sleep(1)

#From main menu
pyautogui.press('down')

time.sleep(1)
pyautogui.typewrite('enter')
#pyautogui.press()#what is the accept button on keyboard
pyautogui.press('left')#move to left team
#find team to play next in bracket

#use pyautogui against a list of teams to find the number of the team and move to them

#move to right team
pyautogui.press('right')
time.sleep(.1)
pyautogui.press('right')
#use function like before to identify team from bracket
#use pyautogui against the list to find the number of the team and move to them


#then do we wait a certain amount of time or check for an image that has the final results?
#could monitor the twitch chat for a !next from streamer
#how to get the results hmm
#update bracket
#start over? if bracket is not compelete


