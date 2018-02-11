import RPi.GPIO as GPIO
import time
import sys

LED = 16
TRIG = 20
ECHO = 21
SENS = 17
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SENS, GPIO.IN)


def main():
	GPIO.output(TRIG,False)
	time.sleep(2)
	simple()
	measure_time()

def measure_time():
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


def simple():
	isHI = False
	isLO = False
	for i in range(1,100):
		GPIO.output(LED,True)
		time.sleep(0.05)
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

if __name__ == "__main__":
    main()
