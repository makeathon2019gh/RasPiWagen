import RPi.GPIO as GPIO
from network import WebSocketAdapter
import time

class MotorAdapter(object):
    pinAntrieb = 2
    pinDirection = 4
    pinStep = 3
    
    def log(self, message):
        print("[Motor] : %s" % message)


    def powerOn(self):
        self.log("Motor wird angeschalten")
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.pinAntrieb, GPIO.HIGH)
    
    def powerOff(self):
        self.log("Motor wird ausgeschalten")
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.pinAntrieb, GPIO.HIGH)
        
    def rechtsFahren(self, count):
        self.log("Fahre nach rechts")
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.pinDirection, GPIO.HIGH)
        for i in range(count):
            GPIO.output(self.pinStep, GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(self.pinStep, GPIO.LOW)
            time.sleep(0.0001)

    def linksFahren(self, count):
        self.log("Fahre nach links")
        GPIO.output(self.pinDirection, GPIO.LOW)
        for i in range(count):
            GPIO.output(self.pinStep, GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(self.pinStep, GPIO.LOW)
            time.sleep(0.0001)

    
    def __init__(self):
        GPIO.setup(self.pinAntrieb, GPIO.OUT)
        GPIO.setup(self.pinSteuerung, GPIO.OUT)
        GPIO.setup(self.pinDirection, GPIO.OUT)


        
