import cv2, sys, socketio
import requests
import numpy as np
import time

from utils import printTimeDiff, initTimeDiff
from client import startListening, curFrame, frameFragments
from random import randint

minMargin = 130
mediumLeftMargin = 130
mediumRightMargin = 350
farMargin = 350

#side is true on the left
#if the opponent has a different color
isDifferent = False
#ipURL = 'http://10.81.176.51/'
ipURL = 'http://10.81.176.207/'

def sprintToLeft(key):
    
    global ipURL
    left = True
    for i in range(4):
        url = ipURL + 'command'
        data = {
          "key": key,
          "commands": {
            "left": left
          }
        }
        response = requests.post(url, json=data)
        left = not(left) #

def sprintToRight(key):
    
    global ipURL
    right = True
    for i in range(4):
        url = ipURL + 'command'
        data = {
          "key": key,
          "commands": {
            "right": right
          }
        }
        response = requests.post(url, json=data)
        right = not(right)

def standLegKick(key):
    
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "down": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.250)

    data = {
      "key": key,
      "commands": {
        "front_kick": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.250)
 
    data = {
      "key": key,
      "commands": {
        "front_kick": False
      }
    }
    response = requests.post(url, json=data)
 
    data = {
      "key": key,
      "commands": {
        "down": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.250)

def teleportLeft(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "down": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "down": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "front_kick": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_kick": False
      }
    }
    response = requests.post(url, json=data) #if you are on the right

def teleportRight(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "down": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "down": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "right": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "right": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "front_kick": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_kick": False
      }
    }
    response = requests.post(url, json=data) #if you are on the left

def sword(key):
    
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data) #close proximity

def damnation(key):
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "back_kick": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "back_kick": False
      }
    }
    response = requests.post(url, json=data) #combo punch

def hellFire(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "down": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "down": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data) #close proximity #close proximity

def spear(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "right": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "right": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data) #if you are on the left #la departare

def takedown(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "right": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "right": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "back_kick": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_kick": False
      }
    }
    response = requests.post(url, json=data) #if you are on the left #la departare

def eternalVegeance(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "back_kick": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_kick": False
      }
    }
    response = requests.post(url, json=data)

def doomBlade(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "right": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "right": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

 
    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020) #best #best

def doomSlice(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

 
    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020) #best

def deadEnd(key):
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)
 
    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data) #best #best

def cataclysm(key):
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "right": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_kick": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

 
    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020) 

    data = {
      "key": key,
      "commands": {
        "back_kick": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "right": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)#best #best #best

def affliction(key):
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)#best #best #best

def block(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "block": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(0.5)
    data = {
      "key": key,
      "commands": {
        "block": False
      }
    }
    response = requests.post(url, json=data)

def frontkick(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "front_kick": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "front_kick": False
      }
    }
    response = requests.post(url, json=data)

def frontpunch(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "front_punch": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "front_punch": False
      }
    }
    response = requests.post(url, json=data)

def backpunch(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "back_punch": True
      }
    }
    response = requests.post(url, json=data)

    data = {
      "key": key,
      "commands": {
        "back_punch": False
      }
    }
    response = requests.post(url, json=data)

def backkick(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "back_kick": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.050)

    data = {
      "key": key,
      "commands": {
        "back_kick": False
      }
    }
    response = requests.post(url, json=data)

def back2(key):   
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    backpunch(key)
    time.sleep(.050)

    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.050)

def hopKick(key):
    
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "right": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.020)

    frontkick(key)
    time.sleep(.050)

    data = {
      "key": key,
      "commands": {
        "right": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.050)

def forward4Right(key):
    
    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "right": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.050)

    backkick(key)
    time.sleep(.050)

    data = {
      "key": key,
      "commands": {
        "right": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.050)

def forward4Left(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "left": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.050)

    backkick(key)
    time.sleep(.050)

    data = {
      "key": key,
      "commands": {
        "left": False
      }
    }
    response = requests.post(url, json=data)
    time.sleep(.050)

def combo1(key):
    global side
    back2(key)
    time.sleep(0.05)
    backpunch(key)
    time.sleep(0.05)
    frontpunch(key)
    time.sleep(0.05)
    backkick(key)
    time.sleep(0.05)
    if side:
        teleportLeft(key)
        side = False
    else:
        teleportRight(key)
        side = True
    time.sleep(0.05)

def combo2(key):
    global side
    if side:
        forward4Right(key)
    else:
        forward4Left(key)
    time.sleep(0.05)
    spear(key)
    time.sleep(0.05)
    backpunch(key)
    time.sleep(0.05)
    frontpunch(key)
    time.sleep(0.05)
    backkick(key)
    time.sleep(0.05)
    if side:
        teleportLeft(key)
        side = False
    else:
        teleportRight(key)
        side = True
    time.sleep(0.05)

def multiPunch(key):
    count = 0
    while(count < 5):
        frontpunch(key)
        count = count + 1

def multiTeleport(key):
    global side
    count = 0
    while(count < 3):
        if side:
            teleportLeft(key)
            frontpunch(key)
            side = False
        else:
            teleportRight(key)
            frontpunch(key)
            side = True
        count = count + 1

def getDown(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "down": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(0.3)
    data = {
      "key": key,
      "commands": {
        "down": False
      }
    }
    response = requests.post(url, json=data)

def jump(key):

    global ipURL
    url = ipURL + 'command'

    data = {
      "key": key,
      "commands": {
        "up": True
      }
    }
    response = requests.post(url, json=data)
    time.sleep(0.05)
    data = {
      "key": key,
      "commands": {
        "up": False
      }
    }
    response = requests.post(url, json=data)

def defense(key):
    k = randint(0,9)
    randFactor = 4
    if k % randFactor == 0:
        block(key)
        time.sleep(0.05)
    if k % randFactor == 1:
        multiPunch(key)
        time.sleep(0.05)
    if k % randFactor == 2:
        getDown(key)
        time.sleep(0.05)
    if k % randFactor == 3:
        jump(key)
        time.sleep(0.05)

def closeAttack(key):
    global side
    k = randint(0,13)
    randFactor = 13
    if k % randFactor == 0:
        combo1(key)
        time.sleep(0.05)
        affliction(key)
    if k % randFactor == 1:
        combo2(key)
        time.sleep(0.05)
        deadEnd(key)
    if k % randFactor == 2:
        standLegKick(key)
        time.sleep(0.05)
        doomSlice(key)
        time.sleep(0.05)
        spear(key)
    if k % randFactor == 3:
        eternalVegeance(key)
        time.sleep(0.05)
        doomBlade(key)
        time.sleep(0.05)
        takedown(key)
    if k % randFactor == 4 or k % randFactor == 5:
        defense(key)
    if k % randFactor == 6:
        deadEnd(key)
    if k % randFactor == 7:
        deadEnd(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        cataclysm(key)
    if k % randFactor == 8:
        affliction(key)
        time.sleep(0.05)
        doomSlice(key)
    if k % randFactor == 9:
        doomSlice(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        affliction(key)
    if k % randFactor == 10:
        deadEnd(key)
    if k % randFactor == 11:
        deadEnd(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        cataclysm(key)
    if k % randFactor == 12:
        affliction(key)
        time.sleep(0.05)
        doomSlice(key)
        
def mediumAttack(key):
    global side
    k = randint(0,15)
    randFactor = 15
    if k % randFactor == 0:
        combo1(key)
        time.sleep(0.05)
        cataclysm(key)
    if k % randFactor == 1:
        combo2(key)
        time.sleep(0.05)
        doomSlice(key)
    if k % randFactor == 2:
        hellFire(key)
        time.sleep(0.05)
        damnation(key)
    if k % randFactor == 3:
        combo2(key)
        time.sleep(0.05)
        damnation(key)
    if k % randFactor == 4:
        getDown(key)
    if k % randFactor == 6:
        deadEnd(key)
    if k % randFactor == 7:
        deadEnd(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        cataclysm(key)
    if k % randFactor == 8:
        affliction(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        doomSlice(key)
    if k % randFactor == 9:
        doomSlice(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        affliction(key)
    if k % randFactor == 10:
        defense(key)
    if k % randFactor == 11:
        farAttack(key)
    if k % randFactor == 12:
        deadEnd(key)
        time.sleep(0.05)
        cataclysm(key)
    if k % randFactor == 13:
        deadEnd(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        cataclysm(key)
    if k % randFactor == 14:
        affliction(key)
        time.sleep(0.05)
        spear(key)
        time.sleep(0.05)
        doomSlice(key)

def farAttack(key):
    global side
    if side:
        teleportLeft(key)
        side = False
        time.sleep(0.05)
        doomBlade(key)
    else:
        teleportRight(key)
        side = True
        time.sleep(0.05)
        doomBlade(key)

def getBlue(contours_blue, leftside, dimx, dimy):

    xmax_blue = 0
    ymax_blue = 0
    xmin_blue = dimx
    ymin_blue = dimy

    maxbluearea = 0
    tmpx_maxblue = 0
    tmpy_maxblue = 0
    tmph_maxblue = 0
    tmpw_maxblue = 0

    for cnt in contours_blue:
        x, y, w, h = cv2.boundingRect(cnt)
        a = w * h
        if leftside:
            if a > maxbluearea and y > dimy / 2 and x < dimx / 2:
                tmpx_maxblue = x
                tmpy_maxblue = y
                tmph_maxblue = h
                tmpw_maxblue = w
                maxbluearea = w * h
        else:
            if a > maxbluearea and y > dimy / 2 and x > dimx / 2:
                tmpx_maxblue = x
                tmpy_maxblue = y
                tmph_maxblue = h
                tmpw_maxblue = w
                maxbluearea = w * h

    for cnt in contours_blue:
        x,y,w,h = cv2.boundingRect(cnt)
        if leftside:
            if y > dimy / 2 and x < dimx / 2:
                deltax = abs(x - tmpx_maxblue)
                deltay = abs(y - tmpy_maxblue)
                if deltax <= 3 * tmpw_maxblue and deltay <= 3 * tmph_maxblue:
                    #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255, 0),2)
                    if x > xmax_blue:
                        xmax_blue = x

                    if y > ymax_blue:
                        ymax_blue = y


                    if x < xmin_blue:
                        xmin_blue = x

                    if y < ymin_blue:
                        ymin_blue = y
        else:
            if y > dimy / 2 and x > dimx / 2:
                deltax = abs(x - tmpx_maxblue)
                deltay = abs(y - tmpy_maxblue)
                if deltax <= 3 * tmpw_maxblue and deltay <= 3 * tmph_maxblue:
                    #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255, 0),2)
                    if x > xmax_blue:
                        xmax_blue = x

                    if y > ymax_blue:
                        ymax_blue = y


                    if x < xmin_blue:
                        xmin_blue = x

                    if y < ymin_blue:
                        ymin_blue = y



    return (xmin_blue, ymin_blue, xmax_blue, ymax_blue)

def getYellow(contours_yellow, leftside, dimx, dimy):
    
    xmax_yellow = 0
    ymax_yellow = 0
    xmin_yellow = dimx
    ymin_yellow = dimy

    for cnt in contours_yellow:
        x,y,w,h = cv2.boundingRect(cnt)
        if not(leftside):
            if y > dimy / 2 and x > dimx / 2:
                if x > xmax_yellow:
                    xmax_yellow = x

                if y > ymax_yellow:
                    ymax_yellow = y


                if x < xmin_yellow:
                    xmin_yellow = x

                if y < ymin_yellow:
                    ymin_yellow = y
        else:
            if y > dimy / 2 and x < dimx / 2:
                if x > xmax_yellow:
                    xmax_yellow = x

                if y > ymax_yellow:
                    ymax_yellow = y


                if x < xmin_yellow:
                    xmin_yellow = x

                if y < ymin_yellow:
                    ymin_yellow = y

    return (xmin_yellow, ymin_yellow, xmax_yellow, ymax_yellow)

def findCharacter((xmin_blue, ymin_blue, xmax_blue, ymax_blue), (xmin_yellow, ymin_yellow, xmax_yellow, ymax_yellow), dimx, dimy):
    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0
    if xmin_yellow == dimx and ymin_yellow == dimy and xmax_yellow == 0 and ymax_yellow == 0:
        xmin = xmin_blue
        ymin = ymin_blue
        xmax = xmax_blue
        ymax = ymax_blue
    elif xmin_blue == dimx and ymin_blue == dimy and xmax_blue == 0 and ymax_blue == 0:
        xmin = xmin_yellow
        ymin = ymin_yellow
        xmax = xmax_yellow
        ymax = ymax_yellow
    else:
        blueArea = (xmax_blue - xmin_blue) * (ymax_blue - ymin_blue)
        yellowArea = (xmax_yellow - xmin_yellow) * (ymax_yellow - ymin_yellow)
        if blueArea > yellowArea:
            xmin = xmin_blue
            ymin = ymin_blue
            xmax = xmax_blue
            ymax = ymax_blue
        else:
            xmin = xmin_yellow
            ymin = ymin_yellow
            xmax = xmax_yellow
            ymax = ymax_yellow
    print `xmin` + " " + `ymin` + " " + `xmax` + " " + `ymax` 
    return (xmin, ymin, xmax, ymax)

def example(frame):    
    global side

    dimx = frame.shape[1]
    dimy = frame.shape[0]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([10,100,20]) #yellow ranges
    upper_red = np.array([20,255,200]) 

    lower_red2 = np.array([105,50, 70]) #blue ranges
    upper_red2 = np.array([110,255,255]) 

    mask = cv2.inRange(hsv, lower_red, upper_red) 
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    xmax_yellow = 0
    ymax_yellow = 0
    xmin_yellow = dimx
    ymin_yellow = dimy

    xmax_blue = 0
    ymax_blue = 0
    xmin_blue = dimx
    ymin_blue = dimy


    #find characters positions
    contours_yellow = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2]
    contours_blue = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2]

    #right
    (xmin_yellow, ymin_yellow, xmax_yellow, ymax_yellow) = getYellow(contours_yellow, False, dimx, dimy)
    (xmin_blue, ymin_blue, xmax_blue, ymax_blue) = getBlue(contours_blue, False, dimx, dimy)

    #we need xminRight, yminRight, xmaxRight, ymaxRight
    xminRight = 0
    yminRight = 0
    xmaxRight = 0
    ymaxRight = 0
    if xmin_yellow == dimx and ymin_yellow == dimy and xmax_yellow == 0 and ymax_yellow == 0:
        xminRight = xmin_blue
        yminRight = ymin_blue
        xmaxRight = xmax_blue
        ymaxRight = ymax_blue
    elif xmin_blue == dimx and ymin_blue == dimy and xmax_blue == 0 and ymax_blue == 0:
        xminRight = xmin_yellow
        yminRight = ymin_yellow
        xmaxRight = xmax_yellow
        ymaxRight = ymax_yellow
        isDifferent = True
        side = True
    else:
        blueArea = (xmax_blue - xmin_blue) * (ymax_blue - ymin_blue)
        yellowArea = (xmax_yellow - xmin_yellow) * (ymax_yellow - ymin_yellow)
        if blueArea > yellowArea:
            xminRight = xmin_blue
            yminRight = ymin_blue
            xmaxRight = xmax_blue
            ymaxRight = ymax_blue
        else:
            xminRight = xmin_yellow
            yminRight = ymin_yellow
            xmaxRight = xmax_yellow
            ymaxRight = ymax_yellow
            isDifferent = True
            side = True


    #left
    (xmin_yellow, ymin_yellow, xmax_yellow, ymax_yellow) = getYellow(contours_yellow, True, dimx, dimy)
    (xmin_blue, ymin_blue, xmax_blue, ymax_blue) = getBlue(contours_blue, True, dimx, dimy)          

    #we need xminLeft, yminLeft, xmaxLeft, ymaxLeft
    xminLeft = 0
    yminLeft = 0
    xmaxLeft = 0
    ymaxLeft = 0
    if xmin_yellow == dimx and ymin_yellow == dimy and xmax_yellow == 0 and ymax_yellow == 0:
        xminLeft = xmin_blue
        yminLeft = ymin_blue
        xmaxLeft = xmax_blue
        ymaxLeft = ymax_blue
    elif xmin_blue == dimx and ymin_blue == dimy and xmax_blue == 0 and ymax_blue == 0:
        xminLeft = xmin_yellow
        yminLeft = ymin_yellow
        xmaxLeft = xmax_yellow
        ymaxLeft = ymax_yellow
        isDifferent = True
        side = False
    else:
        blueArea = (xmax_blue - xmin_blue) * (ymax_blue - ymin_blue)
        yellowArea = (xmax_yellow - xmin_yellow) * (ymax_yellow - ymin_yellow)
        if blueArea > yellowArea:
            xminLeft = xmin_blue
            yminLeft = ymin_blue
            xmaxLeft = xmax_blue
            ymaxLeft = ymax_blue
        else:
            xminLeft = xmin_yellow
            yminLeft = ymin_yellow
            xmaxLeft = xmax_yellow
            ymaxLeft = ymax_yellow
            isDifferent = True
            side = False

    # frame = cv2.rectangle(frame, (xmin_yellow, ymin_yellow), (xmax_yellow, ymax_yellow), (0, 0, 255),2)
    # frame = cv2.rectangle(frame, (xmin_blue, ymin_blue), (xmax_blue, ymax_blue), (0, 0, 255),2)

    frame = cv2.rectangle(frame, (xminRight, yminRight), (xmaxRight, ymaxRight), (0, 255, 0),2)
    frame = cv2.rectangle(frame, (xminLeft, yminLeft), (xmaxLeft, ymaxLeft), (0, 255, 0),2)

    #contours_blue = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2]

    #compute distance between players
    global minMargin, mediumLeftMargin, mediumRightMargin, farMargin
    dist = xminRight - xmaxLeft
    if dist < minMargin:
        closeAttack("bwhci0u9wo0vntio")
    elif dist >= mediumLeftMargin and dist <= mediumRightMargin:
        mediumAttack("bwhci0u9wo0vntio")
    else:
        farAttack("bwhci0u9wo0vntio")

    cv2.imshow('client', frame)
    #cv2.imshow('mask',mask) 
    #cv2.imshow('mask2',mask2) 
    #cv2.imshow('res',res) 
    cv2.waitKey(1)



#global state, side, ipURL
UDP_IP = "10.81.176.170"
UDP_PORT = 5005
if (len(sys.argv) > 1):
    UDP_PORT = int(sys.argv[1])

url = ipURL + 'stream_config'
data = {
  "key": "bwhci0u9wo0vntio",
  "ip": "10.81.176.170",
  "port": UDP_PORT,
  "downscale_ratio": 0.7
}
response = requests.post(url, json=data)

#global state, side
status_url = ipURL + 'get_status'
data = {
  "key": "bwhci0u9wo0vntio"
}
response = requests.post(status_url, json=data)

text = response.text
dictVector = text.split(':')
state = dictVector[-1][:-1]
if state == "p1":
    side = True
else:
    side = False

startListening(UDP_IP, UDP_PORT, example)
