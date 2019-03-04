
from RPi.GPIO import GPIO
from motorik import MotorAdapter
from sensorik import SensorAdapter
from network import WebSocketAdapter
from motorik import Fahrer
from motorik import Location
import string
import random

sensorAdapt = None
motorAdapt = None
webSocketAdapt = None 
token = None
nextLoc = None
fahrer = None

def log(message):
        print("[MAIN] : %s" % message)

def startup():

        log("--------------- Der Einkaufswagen wurde gestartet ---------------")
        
        log("Initialisiere GPIO")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        log("Initialisiere Motor, Websocket und RFID-Adapter")
        motorAdapt = MotorAdapter.MotorAdapter(0,0, webSocketAdapt)
        webSocketAdapt = WebSocketAdapter.WebSocketAdapter("192.168.137.33")
        RFIDAdapter = RFIDAdapter.RFIDAdapter()

        log("Adapter wurden initialisiert.")

        log("Melde beim Server an")
        #Beim Server anmelden
        
        #TODO: Auslesen des ClientSecrets aus Config-File o.ä.
        clientsecret = "KVmKs53uZVmGHcKx"
     
        webSocketAdapt.sendMessage("LOGIN=%s" % clientsecret)

        token = webSocketAdapt.receiveMessage()

        log("Mit ClientSecret \"%s\" beim Server angemeldet und Token \"%s\" als Antwort empfangen, starte RFID-Bereitschaft." % clientsecret, token)

        RFIDAdapter.generateNDEF(token)
        RFIDAdapter.createConnection()

        while(True):
                command = webSocketAdapt.receiveMessage()
                log("Befehl %s vom Server empfangen" % command)

                if(command == "DONE"):
                        log("Der Einkaufswagen ist fertig und kehrt nun wieder in den Anfangszustand zurück.")
                        startup()
                else if(command.startswith('GOTO')):
                        pos = command[5:]
                        nextLoc = Location.Location((int)pos, 'A')
                        self.fahrer = Fahrer.Fahrer(motorAdapt, nextLoc, webSocketAdapt)
                        self.fahrer.startDriving()
                else if(command == "STOP"):
                        log("Der Einkaufswagen wird gestoppt.")
                        self.fahrer.stopDriving()

if __name__ == "__main__":
        startup()
        
