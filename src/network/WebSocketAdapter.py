import websocket
from websocket import create_connection
import time

try:
    import thread
except ImportError:
    import _thread as thread

class WebSocketAdapter(object):
    
    serverip = "127.0.0.1"
    uri = "ws://"+serverip+":80"
    ws = None

    def __init__(self, serverip):
        self.serverip = serverip
        self.log("WebSocket-Serveradresse " + serverip + " initialisiert.")
        self.uri = "ws://"+serverip+":80"
	self.ws = create_connection(self.uri)
	self.log("WebSocket-Verbindung wurde hergestellt")
	
    def sendMessage(self, message):
        self.log("Sende Nachricht \"%s\"" % message)
        self.ws.send(message)
        self.log("Nachricht gesendet.")
        
    def receiveMessage(self):
        self.log("Warte auf Nachricht")
        result = self.ws.recv()
        self.log("Nachricht empfangen \"%s\"" % result)
        return result

    def closeWS(self):
	ws.close()

    def log(self, message):
        print("[WebSocket] : " + message)




