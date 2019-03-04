
import RPi.GPIO as GPIO
from motorik import MotorAdapter
from network import WebSocketAdapter 
from motorik import Fahrer 
import threading

class LinienFolger(threading.Thread):
    pinRight = 27
    pinLeft = 22
    motorAdapt = None
    webSocketAdapt = None
    fahrer = None
    threadid = None

    def __init__(self, fahrer motorAdapt, webSocketAdapt):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

        self.motorAdapt = motorAdapt
        self.webSocketAdapt = webSocketAdapt
        self.fahrer = fahrer

        GPIO.setup(pinRight, GPIO.INPUT)
        GPIO.setup(pinLeft, GPIO.INPUT)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def watch(self):
        log(" Starte Linienfolger")
        while (GPIO.input(pinRight) == 0 and GPIO.input(pinLeft) == 0):
            if(stopped()):
                return
            thread.sleep(0.0001)
        if(GPIO.input(pinRight) == 1 and GPIO.input(pinLeft) == 0 ):
            log("Rechts abgekommmen!")
            while(GPIO.input(pinRight) == 1):
                if(stopped()):
                    return
                motorAdapt.linksFahren(10)
            self.watch()
        else if(GPIO.input(pinRight) == 0 and GPIO.input(pinLeft) == 1):
            log("Links abgekommmen!")
            while(GPIO.input(pinLeft) == 1):
                if(stopped()):
                    return
                motorAdapt.rechtsFahren(10)
            self.watch()    
        else if(GPIO.input(pinRight) == 1 and GPIO.input(pinLeft) == 1):
            log("Von beiden Seiten abgekommmen!")
            motorAdapt.powerOff()
            fahrer.stopDriving()
            webSocketAdapt.sendMessage("LOG=\"Der Wagen ist vom rechten Pfad abgekommen. Bitte manuell beheben.\"")

    def startWatch(self):
        t = threading.Thread(target=watch)
        t.start()

    def stopWatch(self):
        self.stop()

    def log(message):
        print("[Linienfolger] : %s" % message)