"""
my cool mod light
"""

import random


import RPi.GPIO as GPIO
import time
pins = [26,19,6,13,22,27,17,4]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
times = .01
mul = .05

def rol():
    for nu in range(2):
       for blink in pins: 
          GPIO.output(blink, 1)
          time.sleep(.5)
       for blink in [4,17,27,22,13,19,26]: 
          GPIO.output(blink, 0)
          time.sleep(.5)

def bounce():
   times = .01
   mul = .05
   GPIO.setmode(GPIO.BCM)
   try:
         for num in range(10):
            times += mul
            for blink in [21,26,19,13,27,17,4,17,27,13,19,26]:
               GPIO.output(blink, 1)
               time.sleep(times)
               GPIO.output(blink, 0)
               if times >=.2:
                  mul = -.05
                  times = .2
               if times <= .02:
                  mul = .05
                  times = .1
   except KeyboardInterrupt:
      GPIO.setmode(GPIO.BCM)
      for blink in (2):
         GPIO.output(blink, 0)
def coolr():
    GPIO.setmode(GPIO.BCM)
    for n in range(5):
        for blink in [(5,27),(17,13),(19,4)]:
            time.sleep(.36)
            GPIO.output(blink, 1)
            time.sleep(.1)

#GPIO.output(blink, 1)
#print(func)
def rol2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    while True:
           for blink in [26,19,13,27,17,4]: 
                     GPIO.output(blink, 1)
                     time.sleep(.5)
                     GPIO.output(blink, 0)
                     time.sleep(.5)
                     GPIO.cleanup()

def rot():
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    try:
        while True:
            for blink in [13,19,26]: 
                GPIO.output(blink, 1)
                time.sleep(1)
                GPIO.output(blink, 0)

def red():
    



def num():



def fal():



def numb():

#GPIO.output(blink, 1)
   GPIO.cleanup()
#print(func)
except KeyboardInterrupt:
   GPIO.cleanup()
   exit()
paterns = [coolr(),bounce(),rol(),rol2(),rot(),red(),fal(),num(),numb()]
def randit_light():
   return random.choice(paterns)
GPIO.setup(21, GPIO.OUT)

