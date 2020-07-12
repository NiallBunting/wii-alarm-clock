#Libraries
import RPi.GPIO as GPIO
from time import sleep

#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=23
sync=24
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(sync,GPIO.OUT)

# Press sync - will need to connect here
GPIO.output(sync,GPIO.HIGH)
print ("Start Sync")
sleep(0.5) # Delay in seconds
GPIO.output(sync,GPIO.LOW)

#Run forever loop
for x in range(1,5):
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    sleep(0.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beep")
    sleep(0.5)


GPIO.cleanup()
