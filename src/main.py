
import RPi.GPIO as GPIO
from motorik import MotorAdapter
from network import WebSocketAdapter
from motorik import Fahrer
from pathFinding import Location
from sensorik import RFIDAdapter
import string
import random
import sys

sensorAdapt = None
motorAdapt = None
webSocketAdapt = None 
token = None
nextLoc = None
fahrer = None
rfidAdapt = None

def log(message):
        print("[MAIN] : %s" % message)

def startup():
	sys.path.append('/home/pi/RasPiWagen/src')
	sys.path.append('/home/pi/RasPiWagen/src/motorik')
        log("--------------- Der Einkaufswagen wurde gestartet ---------------")

        
        log("Initialisiere GPIO")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        log("Initialisiere Motor, Websocket und RFID-Adapter")
        webSocketAdapt = WebSocketAdapter.WebSocketAdapter("192.168.137.1")
	motorAdapt = MotorAdapter.MotorAdapter()
        
        rfidAdapt = RFIDAdapter.RFIDAdapter()

        log("Adapter wurden initialisiert.")

        log("Melde beim Server an")
        #Beim Server anmelden
        
        #TODO: Auslesen des ClientSecrets aus Config-File o.ae.
        clientsecret = "KVmKs53uZVmGHcKx"
     
        webSocketAdapt.sendMessage("LOGIN=%s" % clientsecret)

        token = webSocketAdapt.receiveMessage()[10:]

        log("Mit ClientSecret \"%s\" beim Server angemeldet und Token \"%s\" als Antwort empfangen, starte RFID-Bereitschaft." % (clientsecret, token))

        rfidAdapt.generateNDEF(token)
        rfidAdapt.createConnection()
	
	fahrer = None
	actLoc = Location.Location(0, 'A')
        while(True):
                command = webSocketAdapt.receiveMessage()
		log("Befehl %s vom Server empfangen" % command)

                if(command == "DONE"):
                        log("Der Einkaufswagen ist fertig und kehrt nun wieder in den Anfangszustand zurueck.")
			webSocketAdapt.closeWS()
                        startup()
                elif(command.startswith('GOTO')):
                        pos = command[5:]
                        nextLoc = Location.Location(pos, 'A')
                        fahrer = Fahrer.Fahrer(motorAdapt, nextLoc, webSocketAdapt, actLoc)
			log("Die aktuelle Location ist %i " % actLoc.getDist()) 
                        fahrer.startDriving()
                elif(command == "BREAK"):
                        log("Der Einkaufswagen wird gestoppt.")
			actLoc = fahrer.getLocation()
                        log("Der aktuelle Abstand betraegt: %i" %actLoc.getDist())
			fahrer.stopDriving()

if __name__ == "__main__":
        startup()
        
