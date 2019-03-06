import time
from motorik import MotorAdapter
from sensorik import LinienFolger
from pathFinding import PathFinder
from pathFinding import Location
from sensorik import UltraschallWatch
from network import WebSocketAdapter
from sensorik import Abstandzaehler
import threading

class Fahrer(threading.Thread):
    linienFolger = None
    motorAdapt = None
    pathFinder = None
    destLoc = None
    ultraSchallWatcher = None
    webSocketAdapter = None
    abstandZaehler = None
    actLoc = None

    def __init__(self, motorAdapt, destLoc, webSocketAdapt, actLoc):
#        super(StoppableThread, self).__init__()
	threading.Thread.__init__(self)
        self._stop_event = threading.Event()
	self.actLoc = actLoc
        self.linienFolger = LinienFolger.LinienFolger(self, motorAdapt, webSocketAdapt)
        self.motorAdapt = motorAdapt
        self.pathFinder = PathFinder.PathFinder(self.actLoc)
        self.abstandZaehler = Abstandzaehler.Abstandzaehler(self.pathFinder)
        self.destLoc = destLoc
        self.webSocketAdapt = webSocketAdapt
        self.ultraSchallWatcher = UltraschallWatch.UltraschallWatch(self, motorAdapt, webSocketAdapt)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def getLocation(self):
	return self.actLoc

    def run(self):
        self.log("Fahrer gestartet. Starte Watcher")
        
        #self.ultraSchallWatcher.startWatch()
        #self.linienFolger.startWatch()
        self.abstandZaehler.startMonitoring()
        self.motorAdapt.powerOn()

        self.log("Starte Motor")

        while(self.pathFinder.getDistanceToLoc(self.destLoc) > 100):
	    time.sleep(0.001)
	    if(self.stopped()):
		time.sleep(0.1)
            	self.actLoc = self.pathFinder.getLocation()
		self.log("Breche Fahrt ab")
                self.motorAdapt.powerOff()
                #self.ultraSchallWatcher.stopWatch()
                #self.linienFolger.stopWatch()
                self.abstandZaehler.stopMonitoring()
                
                return
            continue
        self.actLoc = self.pathFinder.getLocation()
        self.log("Ziel erreicht.")
        self.motorAdapt.powerOff()

        #self.ultraSchallWatcher.stopWatch()
        #self.linienFolger.stopWatch()
        self.abstandZaehler.stopMonitoring()

    def startDriving(self):
        self.start()

    def stopDriving(self):
        self.stop()

    def log(self, message):
        print("[Fahrer] : %s" % message)


