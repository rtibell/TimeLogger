#!/usr/bin/python
import sys
import time
import RPi.GPIO as GPIO
from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rw=21, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)

humidity = 80
temperature = 18
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("*** Start ***")
time.sleep(5)    
lcd.clear()
lcd.cursor_pos = (0, 0)

while True:
    print("Temp: %d C" % temperature)
    print("Humidity: %d %%" % humidity)
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: %d C" % temperature)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: %d %%" % humidity)
    time.sleep(3)    
    humidity = humidity - 2
    temperature = temperature + 1
