import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
#PIO.output(7, GPIO.LOW)
#GPIO.output(7, GPIO.LOW)
while True:
   val=input("1 for on, 0 for off: ")
   if val=='1':
       GPIO.output(7, GPIO.HIGH)
   else:
       GPIO.output(7, GPIO.LOW)
   print(val)