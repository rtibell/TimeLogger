import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(22, GPIO.OUT)


for i in range(1,100):
	time.sleep(0.5)
	sens = GPIO.input(17)
	if sens == 1:
		print "found item"
	elif sens == 0:
		print "no item found"


