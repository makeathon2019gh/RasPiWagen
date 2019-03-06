
import RPi.GPIO as GPIO
from motorik import MotorAdapter
from network import WebSocketAdapter
import motorik.Fahrer
import threading
import time

class LinienFolger(threading.Thread):
    pinRight = 27
    pinLeft = 22
    motorAdapt = None
    webSocketAdapt = None
    fahrer = None
    threadid = None

    def __init__(self, fahrer, motorAdapt, webSocketAdapt):
        #super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

        self.motorAdapt = motorAdapt
        self.webSocketAdapt = webSocketAdapt
        self.fahrer = fahrer

        GPIO.setup(self.pinRight, GPIO.INPUT)
        GPIO.setup(self.pinLeft, GPIO.INPUT)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        self.log(" Starte Linienfolger")
        while (GPIO.input(self.pinRight) == 0 and GPIO.input(self.pinLeft) == 0):
            if(self.stopped()):
                return
            time.sleep(0.0001)
        if(GPIO.input(self.pinRight) == 1 and GPIO.input(self.pinLeft) == 0 ):
            self.log("Rechts abgekommmen!")
            while(GPIO.input(self.pinRight) == 1):
                if(self.stopped()):
                    return
                self.motorAdapt.linksFahren(10)
            self.run()
        elif(GPIO.input(self.pinRight) == 0 and GPIO.input(self.pinLeft) == 1):
            self.log("Links abgekommmen!")
            while(GPIO.input(self.pinLeft) == 1):
                if(self.stopped()):
                    return
                self.motorAdapt.rechtsFahren(10)
            self.run()    
        elif(GPIO.input(self.pinRight) == 1 and GPIO.input(self.pinLeft) == 1):
            self.log("Von beiden Seiten abgekommmen!")
            self.motorAdapt.powerOff()
            self.fahrer.stopDriving()
            self.webSocketAdapt.sendMessage("LOG=\"Der Wagen ist vom rechten Pfad abgekommen. Bitte manuell beheben.\"")

    def startWatch(self):
        self.start()

    def stopWatch(self):
        self.stop()

    def log(self, message):
        print("[Linienfolger] : %s" % message)
