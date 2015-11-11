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
    for blink in [(6,27),(17,13),(19,4)]:
        time.sleep(.01)
        GPIO.output(blink, 1)
        GPIO.output(blink, 0)

#GPIO.output(blink, 1)
        time.sleep(.5)
#print(func)
def rol2():
    GPIO.setmode(GPIO.BCM)
    
paterns = [coolr(),bounce(),rol()]
def randit_light():
   return random.choice(paterns)

