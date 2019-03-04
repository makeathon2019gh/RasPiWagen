import RPi.GPIO as GPIO
from motorik import MotorAdapter
from network import WebSocketAdapter
from motorik import Fahrer
import threading

class UltraschallWatch(threading.Thread):
    pinUltra1 = 5
    pinUltra2 = 6
    pinUltra3 = 13
    pinUltra4 = 19
    pinUltra5 = 26

    pinTrigger = 21

    motorAdapt = None
    webSocketAdapt = None
    fahrer = None

    def __init__(self, fahrer, motorAdapt, webSocketAdapt):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

        GPIO.setup(pinUltra1, GPIO.IN)
        GPIO.setup(pinUltra2, GPIO.IN)
        GPIO.setup(pinUltra3, GPIO.IN)
        GPIO.setup(pinUltra4, GPIO.IN)
        GPIO.setup(pinUltra5, GPIO.IN)
        
        GPIO.setup(pinTrigger, GPIO.OUT)
        
        self.motorAdapt = motorAdapt
        self.webSocketAdapt = webSocketAdapt
        self.fahrer = fahrer

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


    def watch(self):
        log(" Beginne Ultraschall-Überwachung")
        while(True):
            if(stopped()):
                return
            
            GPIO.output(pinTrigger, True)
            time.sleeep(0.00001)
            GPIO.output(pinTrigger, False)

            StartZeit = time.time()
            EndZeit = StartZeit

            while (GPIO.input(pinUltra1) == 0 and GPIO.input(pinUltra2) == 0 and GPIO.input(pinUltra3) == 0 and GPIO.input(pinUltra4) == 0 and GPIO.input(pinUltra5) == 0):
                continue
            
            StartZeit = time.time()

            while (GPIO.input(pinUltra1) == 1 or GPIO.input(pinUltra2) == 1 or GPIO.input(pinUltra3) == 1 or GPIO.input(pinUltra4) == 1 or GPIO.input(pinUltra5) == 1):
                continue
            
            EndZeit = time.time()
            Dauer = EndZeit - StartZeit
            distanz = (Dauer * 34300 ) / 2
            
            if(distanz < 50):
                motorAdapt.powerOff()
                fahrer.stopDriving()
                log(" Distanz &.1f wurde gemessen und als zu kurz befunden." % distanz)
                webSocketAdapt.sendMessage("STOP")
                webSocketAdapt.sendMessage("LOG=\"Hindernis im Weg!!! Bitte nichts näher als 50cm an den Wagen herankommen lassen!\"")
            
    def startWatch(self):
        t = threading.Thread(target=watch)
        t.start()

    def stopWatch(self):
        self.stop()

    def log(message):
        print("[Ultraschall] : %s" % message)


            
    