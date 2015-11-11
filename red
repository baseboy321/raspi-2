#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
   
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
