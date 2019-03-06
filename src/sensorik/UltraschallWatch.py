import time
import RPi.GPIO as GPIO
from motorik import MotorAdapter
from network import WebSocketAdapter
import motorik.Fahrer
import threading

class UltraschallWatch(threading.Thread):
    pinUltra1 = 5
    pinUltra2 = 6
    pinUltra3 = 13
    pinUltra4 = 19
    pinUltra5 = 26
    pinUltra6 = 23
    pinUltra7 = 24
    pinUltra8 = 25
    pinUltra9 = 8

    pinTrigger = 21

    motorAdapt = None
    webSocketAdapt = None
    fahrer = None

    def __init__(self, fahrer, motorAdapt, webSocketAdapt):
        #super(StoppableThread, self).__init__()
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pinUltra1, GPIO.IN)
        GPIO.setup(self.pinUltra2, GPIO.IN)
        GPIO.setup(self.pinUltra3, GPIO.IN)
        GPIO.setup(self.pinUltra4, GPIO.IN)
        GPIO.setup(self.pinUltra5, GPIO.IN)
        GPIO.setup(self.pinUltra6, GPIO.IN)
        GPIO.setup(self.pinUltra7, GPIO.IN)
        GPIO.setup(self.pinUltra8, GPIO.IN)
        GPIO.setup(self.pinUltra9, GPIO.IN)
        
        GPIO.setup(self.pinTrigger, GPIO.OUT)
        
        self.motorAdapt = motorAdapt
        self.webSocketAdapt = webSocketAdapt
        self.fahrer = fahrer

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def watch(self):
        self.log(" Beginne Ultraschall-Ueberwachung")
        while(True):
	    time.sleep(0.01)
            if(self.stopped()):
                return
            
            GPIO.output(self.pinTrigger, True)
            time.sleep(0.00001)
            GPIO.output(self.pinTrigger, False)

            StartZeit = time.time()
            EndZeit = StartZeit

            while (GPIO.input(self.pinUltra1) == 0 and GPIO.input(self.pinUltra2) == 0 and GPIO.input(self.pinUltra3) == 0 and GPIO.input(self.pinUltra4) == 0 and GPIO.input(self.pinUltra5) == 0  and GPIO.input(self.pinUltra6) == 0 and GPIO.input(self.pinUltra7) == 0 and GPIO.input(self.pinUltra8) == 0 and GPIO.input(self.pinUltra9) == 0):
                continue
            
            StartZeit = time.time()

            while (GPIO.input(self.pinUltra1) == 1 or GPIO.input(self.pinUltra2) == 1 or GPIO.input(self.pinUltra3) == 1 or GPIO.input(self.pinUltra4) == 1 or GPIO.input(self.pinUltra5) == 1 or GPIO.input(self.pinUltra6) == 1 or GPIO.input(self.pinUltra7) == 1 or GPIO.input(self.pinUltra8) == 1 or GPIO.input(self.pinUltra9) == 1):
                continue
            
            EndZeit = time.time()
            Dauer = EndZeit - StartZeit
            distanz = (Dauer * 34300 ) / 2
            
            if(distanz < 50):
                self.motorAdapt.powerOff()
                self.fahrer.stopDriving()
                self.log(" Distanz &.1f wurde gemessen und als zu kurz befunden." % distanz)
                self.webSocketAdapt.sendMessage("STOP")
                self.webSocketAdapt.sendMessage("LOG=\"Hindernis im Weg!!! Bitte nichts naeher als 50cm an den Wagen herankommen lassen!\"")
            
    def startWatch(self):
        self.start()

    def stopWatch(self):
        self.stop()

    def log(self, message):
        print("[Ultraschall] : %s" % message)


            
    
