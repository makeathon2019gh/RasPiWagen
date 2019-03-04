from RPi.GPIO import GPIO
from network import WebSocketAdapter

class MotorAdapter(object):
    pinAntrieb = 2
    pinDirection = 4
    pinStep = 3
    webSocketAdapt = None

    def log(message):
        print("[Motor] : %s" % message)


    def powerOn(self):
        log("Motor wird angeschalten")
        GPIO.output(pinAntrieb, 1)
    
    def powerOff(self):
        log("Motor wird ausgeschalten")
        GPIO.output(pinAntrieb, 0)
        
    def rechtsFahren(count):
        log("Fahre anch rechts")
        GPIO.output(pinDirection, High)
        for i in range(count):
            GPIO.output(pinStep, High)
            time.sleep(0.0001)
            GPIO.output(pinStep, Low)
            time.sleep(0.0001)

    def linksFahren(count):
        log("Fahre anch links")
        GPIO.output(pinDirection, Low)
        for i in range(count):
            GPIO.output(pinStep, High)
            time.sleep(0.0001)
            GPIO.output(pinStep, Low)
            time.sleep(0.0001)

    
    def __init__(self, pinAntrieb, pinSteuerung, webSocketAdapt):
        self.pinAntrieb = pinAntrieb
        self.pinSteuerung = pinSteuerung
        self.webSocketAdapt = webSocketAdapt
        GPIO.setup(pinAntrieb, GPIO.OUT)
        GPIO.setup(pinSteuerung, GPIO.OUT)
    


        