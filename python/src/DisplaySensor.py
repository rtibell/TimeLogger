#!/usr/bin/python
from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time
import sys

#BCD
#----
LED = 36 #16
TRIG = 38 #20
ECHO = 40 #21
SENS = 15 #22
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SENS, GPIO.IN)

#BOARD
#------
LCD_RW = 21
LCD_RS = 37
LCD_E = 35
LCD_D0 = 23
LCD_D1 = 29
LCD_D2 = 31
LCD_D3 = 33
lcd = CharLCD(cols=16, rows=2, pin_rw=LCD_RW, pin_rs=LCD_RS, pin_e=LCD_E, pins_data=[LCD_D3, LCD_D2, LCD_D1, LCD_D0], numbering_mode=GPIO.BOARD)
dsp_line1 = ""
dsp_line2 = ""

def main():
	lcd.clear()
	lcd.cursor_pos = (0, 0)
	GPIO.output(TRIG,False)
	time.sleep(2)
	#simple()
	measure_time()

def measure_time():
	GPIO.output(LED,False)
	for i in range(1,20):
		time.sleep(0.5)
		GPIO.output(TRIG,True)
		time.sleep(0.00001)
		GPIO.output(TRIG,False)
		pulse_start = time.time()
		while GPIO.input(ECHO)==0:
			pulse_start = time.time()
		pulse_end = time.time()
		while GPIO.input(ECHO)==1:
			pulse_end = time.time()
		print pulse_start
		print pulse_end
		delta = (pulse_end - pulse_start)
		speed = 34300.0 * delta / 200.0
		print delta
		print speed
		print "----------"
		if speed > 1.0:
			GPIO.output(LED,True)
		else:
			GPIO.output(LED,False)
		dsp("Distance: %1.2f" % speed, "Sensor: %d" % GPIO.input(SENS))


def simple():
	isHI = False
	isLO = False
	GPIO.output(LED,True)
	for i in range(1,100):
		time.sleep(0.1)
		sens1 = GPIO.input(ECHO)
		if sens1 == True:
			isHI = True
		if sens1 == False:
			isLO = True
		GPIO.output(TRIG,True)
		time.sleep(0.0001)
		GPIO.output(TRIG,False)
		sens2 = GPIO.input(ECHO)
		time.sleep(0.0001)
		sens3 = GPIO.input(ECHO)
		print "values " + str(sens1) + " " + str(sens2) + " " + str(sens3) +  " |  " + str(GPIO.input(SENS)) + " |  " + str(isHI) + " " + str(isLO)

	GPIO.output(LED,False)

def dsp(line1, line2):
	lcd.cursor_pos = (0, 0)
	lcd.write_string(line1)
	lcd.cursor_pos = (1, 0)
	lcd.write_string(line2)


if __name__ == "__main__":
    main()
