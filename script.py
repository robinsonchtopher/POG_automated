import socketserver
from turtle import down
import pyautogui
import time
import keyboard
import numpy as np
import random
#import win32api, win32con
import socket
import logging
from emoji import demojize#to decode emoji
import re

#from main menu, navigate to the exhibition, pick both teams, move to middle(no team selected to control) and start game, after game get score?, update the bracket, find next game to sim
#bracketHQ
"""
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


#k for A, l for B

#teams=["jacksonville", "arizona", "denver", "miami", "dallas"]
"""


#new situation
""" So what I want now is to have an exhibition started and then this program to be ran, 
Action 1: start game from cpu vs cpu position
Action 2: wait for game to finish, wait for command in twitch chat, or wait for end game screen
Action 3: conclude the game
Action 4: 
"""
#pogflbot
#Password oauth:gl8h5tz6q7vs5k8l15qki2tm965hj6

sock=socket.socket()


server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'pogflbot'
token = 'oauth:gl8h5tz6q7vs5k8l15qki2tm965hj6'
channel = '#jax_existz'

sock.connect((server, port))
#encode('utf-8') encodes the string to bytes so it can be sent over the socket
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))
#carries the channel we want to watch
resp=sock.recv(2048).decode('utf-8')

print(resp)
#sock.close()
logging.basicConfig(level=logging.DEBUG,#debug allows all levels of logging to be written
                    format='%(asctime)s — %(message)s',#look of the file, time recorded the line and message separated by a dash
                    datefmt='%Y-%m-%d_%H:%M:%S', #how the time portion is recorded
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])#logging to chat.log, could add another handler to print
#should also add a more dynamic name for better filing
logging.info(resp)

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    
    elif len(resp) > 0:
        logging.info(demojize(resp))
        print("I'm printing")
        print(resp)
        result = re.split(r"[:!-;,.\s]\s*", resp)
        print(result)
        print(result[1])
        print(result[(len(result)-2)])
        #if result[1] == 'jax_existz AND result[(len(result)-2)] in botCommands:
            #bot.result[(len(result)-2)]
        

