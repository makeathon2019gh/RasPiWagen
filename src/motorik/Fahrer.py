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

    def __init__(self, motorAdapt, destLoc, webSocketAdapt):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

        linienFolger = LinienFolger.LinienFolger(motorAdapt, webSocketAdapt)
        self.motorAdapt = motorAdapt
        self.pathFinder = PathFinder.PathFinder()
        self.abstandZaehler = Abstandzaehler.Abstandzaehler(pathFinder)
        self.destLoc = destLoc
        self.webSocketAdapt = webSocketAdapt
        self.ultraSchallWatcher = UltraSchallWatch.UltraschallWatch(motorAdapt, webSocketAdapt)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


    def drive(self):
        
        log("Fahrer gestartet.")
        
        ultraSchallWatcher.startWatch()
        linienFolger.startWatch()
        abstandZaehler.startMonitoring()
        motorAdapt.powerOn()

        while(pathFinder.getDistanceToLoc(destLoc) > 0.1):
            if(stopped()):
                ultraSchallWatcher.stopWatch()
                linienFolger.stopWatch()
                abstandZaehler.stopMonitoring()
                return
            continue
        
        log("Ziel erreicht.")

        ultraSchallWatcher.stopWatch()
        linienFolger.stopWatch()
        abstandZaehler.stopMonitoring()

    def startDriving(self):
        t = threading.Thread(target=drive)
        t.start()

    def stopDriving(self):
        stop()

    def log(message):
        print("[Fahrer] : %s" % message)


