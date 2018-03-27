#!/usr/bin/env python
import RPi.GPIO as GPIO # RPi.GPIO can be referred as GPIO from now
import time
 
ledPin7 = 7    # pin7
ledPin11 = 11    # pin11
ledPin13 = 13    # pin13
sleep = .1
 
def setup():
        GPIO.setmode(GPIO.BOARD)       # GPIO Numbering of Pins
        GPIO.setup(ledPin7, GPIO.OUT)   # Set ledPin as output
        GPIO.output(ledPin7, GPIO.LOW)  # Set ledPin to LOW to turn Off the LED

        GPIO.setup(ledPin11, GPIO.OUT)   # Set ledPin as output
        GPIO.output(ledPin11, GPIO.LOW)  # Set ledPin to LOW to turn Off the LED

        GPIO.setup(ledPin13, GPIO.OUT)   # Set ledPin as output
        GPIO.output(ledPin13, GPIO.LOW)  # Set ledPin to LOW to turn Off the LED
 
def loop():
        while True:
                print 'LED on'
                GPIO.output(ledPin7, GPIO.HIGH)   # LED On
                time.sleep(sleep)                  # wait 1 sec
                print 'LED off'
                GPIO.output(ledPin7, GPIO.LOW)   # LED Off
                time.sleep(sleep)                 # wait 1 sec

                print 'LED on'
                GPIO.output(ledPin11, GPIO.HIGH)   # LED On
                time.sleep(sleep)                  # wait 1 sec
                print 'LED off'
                GPIO.output(ledPin11, GPIO.LOW)   # LED Off
                time.sleep(sleep)                 # wait 1 sec

                print 'LED on'
                GPIO.output(ledPin13, GPIO.HIGH)   # LED On
                time.sleep(sleep)                  # wait 1 sec
                print 'LED off'
                GPIO.output(ledPin13, GPIO.LOW)   # LED Off
                time.sleep(sleep)                 # wait 1 sec
def endprogram():
 
        GPIO.output(ledPin7, GPIO.LOW)     # LED Off
        GPIO.output(ledPin11, GPIO.LOW)     # LED Off
        GPIO.output(ledPin13, GPIO.LOW)     # LED Off
        GPIO.cleanup()                    # Release resources
 
if __name__ == '__main__':         # Program starts from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the destroy() will be  executed.
                endprogram()

