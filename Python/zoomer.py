import RPi.GPIO as GPIO
import time
 
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
#input_value = GPIO.input(17)
GPIO.output(4, GPIO.HIGH)
time.sleep(1)
GPIO.output(4, GPIO.LOW)

 
