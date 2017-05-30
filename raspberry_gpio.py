## Last edited by Milton Li 30 May 2017
## Raspberry GPIO for temperature sensing

import RPi.GPIO as GPIO
import time

# Sensor input pin number of the R-Pi
## Change this according to which pin is used as input
pinNumber = 3

# Intervals at which to take temperature readings (seconds)
t = 30

# Sets up the GPIO pin, pull-down to default to 0 V
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        # Check if the GPIO has any input
        if GPIO.input(pinNumber) > 0:
            print ("Temperature sensed: ", GPIO.input(pinNumber))
    # Sleep for t seconds
    time.sleep(t)        
    
    # Detect if temperature is rising and then call the my_callback() method
    GPIO.add_event_detect(pinNumber, GPIO.RISING)
    GPIO.add_event_callback(pinNumber, my_callback)
    
finally:
    GPIO.cleanup()

# Callback event: Do this if temperature is rising
def my_callback():
    print ("Temperature rising!")
    