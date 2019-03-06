
import RPi.GPIO as GPIO
from pathFinding import PathFinder
import threading
import time

class Abstandzaehler(threading.Thread):

    pinIRRecv = 17
    pathFinder = None

    def __init__(self, pathFinder):
#        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

        self.pathFinder = pathFinder
        GPIO.setup(self.pinIRRecv, GPIO.IN)
        pass

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        self.log(" Abstandzaehler wird gestartet")
        while(True):
            if(self.stopped()):
                return
            while(GPIO.input(self.pinIRRecv) == True):
                if(self.stopped()):
                    return
                time.sleep(0.0001)
                self.pathFinder.updateLocation(62.831)
            while(GPIO.input(self.pinIRRecv) == False):
                if(self.stopped()):
                    return
                time.sleep(0.0001)
            
    def startMonitoring(self):
        self.start()

    def stopMonitoring(self):
        self.stop()

    def log(self, message):
        print("[Abstandzaehler] : %s" % message)


