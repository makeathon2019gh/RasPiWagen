
import RPi.GPIO as GPIO
from MotorAdapter import MotorAdapter
from WebSocketAdapter import WebSocketAdapter 
import threading

class LinienFolger(threading.Thread):
    pinRight = 27
    pinLeft = 22
    motorAdapt = None
    webSocketAdapt = None
    threadid = None

    def __init__(self, motorAdapt, webSocketAdapt):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

        self.motorAdapt = motorAdapt
        self.webSocketAdapt = webSocketAdapt

        GPIO.setup(pinRight, GPIO.INPUT)
        GPIO.setup(pinLeft, GPIO.INPUT)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def watch(self):
        while (GPIO.input(pinRight) == 0 and GPIO.input(pinLeft) == 0):
            if(stopped()):
                return
            thread.sleep(0.0001)
        if(GPIO.input(pinRight) == 1 and GPIO.input(pinLeft) == 0 ):
            while(GPIO.input(pinRight) == 1):
                if(stopped()):
                    return
                motorAdapt.linksFahren(10)
            self.watch()
        else if(GPIO.input(pinRight) == 0 and GPIO.input(pinLeft) == 1):
            while(GPIO.input(pinLeft) == 1):
                if(stopped()):
                    return
                motorAdapt.rechtsFahren(10)
            self.watch()    
        else if(GPIO.input(pinRight) == 1 and GPIO.input(pinLeft) == 1):
            motorAdapt.powerOff()
            webSocketAdapt.sendMessage("LOG=\"Der Wagen ist vom rechten Pfad abgekommen. Bitte manuell beheben.\"")

    def startWatch(self):
        t = threading.Thread(target=watch)
        t.start()

    def stopWatch(self):
        self.stop()