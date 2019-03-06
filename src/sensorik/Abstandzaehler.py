
import RPi.GPIO as GPIO
from pathFinding import PathFinder
import threading
import time

class Abstandzaehler(threading.Thread):

    pinIRRecv = 17
    pathFinder = None

    def __init__(self, pathFinder):
#        super(StoppableThread, self).__init__()
        threading.Thread.__init__(self)

        self._stop_event = threading.Event()

        self.pathFinder = pathFinder
        GPIO.setup(self.pinIRRecv, GPIO.IN)
        pass

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(self.pinIRRecv, GPIO.IN)
        self.log(" Abstandzaehler wird gestartet")
        while(True):
	    time.sleep(0.001)
            if(self.stopped()):
                return
            while(GPIO.input(self.pinIRRecv) == True):
                self.log("Abstandzaehler hat eine Umdrehung festgestellt.")
		if(self.stopped()):
                    return
                time.sleep(0.01)
                self.pathFinder.updateLocation(83.5)
		break
            while(GPIO.input(self.pinIRRecv) == False):
                if(self.stopped()):
                    return
                time.sleep(0.01)
            
    def startMonitoring(self):
        self.start()

    def stopMonitoring(self):
        self.stop()

    def log(self, message):
        print("[Abstandzaehler] : %s" % message)


