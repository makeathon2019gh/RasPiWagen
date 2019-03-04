
import RPi.GPIO as GPIO
from pathFinding import PathFinder
import threading

class Abstandzaehler(threading.Thread):

    pinIRRecv = 17
    pathFinder = None

    def __init__(self, pathFinder):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

        self.pathFinder = pathFinder
        GPIO.setup(pinIRRecv, GPIO.IN)
        pass

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


    def monitoring(self)
        log(" Abstandzähler wird gestartet")
        while(True):
            if(stopped()):
                return
            while(GPIO.input(pinIRRecv) == True):
                if(stopped()):
                    return
                time.sleep(0.0001)
                pathFinder.updateLocation(62.831)
            while(GPIO.input(pinIRRecv) == False):
                if(stopped()):
                    return
                time.sleep(0.0001)
            
    def startMonitoring(self):
        t = threading.Thread(target = monitoring)
        t.start()

    def stopMonitoring(self):
        stop()

    def log(message):
        print("[Abstandzähler] : %s" % message)


