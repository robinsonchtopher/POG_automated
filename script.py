#import socketserver
from turtle import down
from xmlrpc.client import Unmarshaller
import pyautogui
import time
#import keyboard
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
#notes already have game ready to go on the exhibition screen, have stream running
#start this app and then tab back into the Legends Bowl game
time.sleep(2)#delayed start to tab into the game

class Robit:
    def __init__(self, streamer):
        self.streamer = streamer
        self.inGame = False # not sure which of these options is better at this point
        self.screen = 'menu' #I'm thinking options are: menu, game, end
        self.actions = ['up','down','left','right','enter','back', 'start', 'end', 'commands', 'skip', 'findgame']
    def __str__(self):
        return f"{self.streamer}"
    #what all do I need the bot to do, option for each input up, down, right left, enter, back
    #then have a function for end game, start game, skip game, 
    def up(self):
        pyautogui.press('w')
        time.sleep(1)

    def left(self):
        pyautogui.press('a')
        time.sleep(1)

    def down(self):
        #presses down on the keyboard
        pyautogui.press('s')
        time.sleep(1)

    def right(self):

        pyautogui.press('d')
        time.sleep(1)

    def enter(self):
        pyautogui.keyDown('k')#k is the enter key for legends bowl
        time.sleep(1)
        pyautogui.keyUp('k')
        time.sleep(1)

    def back(self):
        """#presses the L key which this will move to the previous screen, this is equivilent to the B button on a controller 
        if self.inGame == True:#do not want to mess with things if a game is being played
            print("the mesage below this")
            #send message I think the game is currently still being played, type #end to end game
        else:
            #pyautogui.press('l')# L is the key to go back in Legends Bowl
            """
        pyautogui.keyDown('l')
        time.sleep(1)
        pyautogui.keyUp('l')
        time.sleep(1)

    def start(self):
        #from looking at the game this will enter the game and start it from the cpu vs cpu position
        self.enter()
        self.down()
        self.enter()
        self.enter()
        self.inGame=True

    def end(self):
        #this function will end the game from the ending screen and take you to the 
        if self.inGame ==True:
            self.back()
            self.enter()
            self.enter()
            time.sleep(5)#give the game time to load the menu
            #try 16 times to set game ingame to false if it never passes then keep change week
            gamesplayed=0
            self.findgame()
                         
               

    def findgame(self):
        gamesplayed=0
        for i in range(0,15):
            print(pyautogui.pixel(1670,1041)[1])
            print(gamesplayed)
            if pyautogui.pixel(1670,1041)[1] >= 150:#check if the green value is over 150 the actual value is about 180 
                self.inGame=False
            else:
                if gamesplayed <= 14:
                    self.down()
                    gamesplayed+=1
                else:
                    self.nextweek()       
            

    def reset(self):
        #if you have given commands that leave you in a spot you are unsure how to get back to the games use this function to reset back to the exhibition menu
        self.back()
        self.back()
        self.back()
        self.back()
        self.back()
        self.back()
        self.down()
        self.enter()

    def mainmenu(self):
        #use this function to go to the starting screen of legends bowl(hopefully)
        self.back()
        self.back()
        self.back()
        self.back()
        self.back()
        self.back()


    def skip(self):
        if self.inGame == True:
            print("send message I think the game is currently still being played, type #end to end game")
        else:
            self.down()
            print("Start this game? This can be done using the start command!")
    
    def commands(self):
        print("These are the available commands " + str(self.actions))
    
    def nextweek(self):

        self.right()

    def previousweek(self):

        self.left()
    
    def chat(self,msg):
        sock.send(f"PRIVMSG {msg}\n".encode('utf-8'))
        sock.send("PRIVMSG {} :{}\n".format(channel, msg).encode('utf-8'))
    








    
time.sleep(5)
goLive=Robit('jax_existz')
print("POGFLBOT is ready to start the game!")







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
"""
logging.basicConfig(level=logging.DEBUG,#debug allows all levels of logging to be written
                    format='%(asctime)s — %(message)s',#look of the file, time recorded the line and message separated by a dash
                    datefmt='%Y-%m-%d_%H:%M:%S', #how the time portion is recorded
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])#logging to chat.log, could add another handler to print
#should also add a more dynamic name for better filing
logging.info(resp)"""

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
        print(result[(len(result)-2)])#quoted out the streamer requirement for testing purposes
        """if result[1] == goLive.streamer:
            if result[(len(result)-2)] in goLive.actions:
                #goLive.(result[(len(result)-2)])()
                getattr(goLive, (result[(len(result)-2)]))()
            else:
                print("this is not an action I can take")
        else:
            print("this is not the streamer")
            """
        if result[(len(result)-2)] in goLive.actions:
                #goLive.(result[(len(result)-2)])()
                getattr(goLive, (result[(len(result)-2)]))()
        else:
                print("this is not an action I can take")

teams={}            
def tournament():
    #for each of the 32 teams assign a random value
    for i in teams:
        teams[i][2]=random(1,32)#that has not been selected
    #identify the location of each team in the list of teams

    #find the shortest path to selecting them or just press that many times
    #start game, wait for end of game, can be twitch could be look for end game screen colors
    #start next game, should finish first round games then go to second round, etc.
    #at the end maybe do something? and output the bracket as we go so the winner can be easily seen



#look into discord notification, this will not work without another account which requires cell phone verification lol
#for exhibition post game takes you to main menu, press A to go in
#for exhibition tournanet,  how do I see who wins? wait for twitch input to decalre the winner?
#need to see how to chat with the bot
