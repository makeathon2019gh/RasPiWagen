import websocket
import asyncio
import time
try:
    import thread
except ImportError:
    import _thread as thread

class WebSocketAdapter(object):
    
    serverip = "127.0.0.1"
    uri = "ws://"+serverip+":80"

    def __init__(self, serverip):
        self.serverip = serverip
        self.log("WebSocket-Serveradresse " + serverip + " initialisiert.")
        self.uri = "ws://"+serverip+":80"

    def on_message(ws, message):
        self.log(message)

    def on_error(ws, error):
        self.log("Fehler %s" % error)

    def on_close(ws):
        self.log("Connection closed")

    def on_open(ws):
        def run(*args):
            ws.close()
            log("Terminating WS-Thread")
        thread.start_new_thread(run, ())

    def listenForMessage():
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(uri, on_message = on_message, on_error = on_error, on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()

    def sendMessage(self, message):
        ws = create_connection(uri)
        log("Sending message \"%s\"" % message)
        ws.send(message)
        log("Message sent.")
        ws.close()

    def receiveMessage(self):
        ws = create_connection(uri)
        log("Waiting for message")
        result = ws.recv()
        log("Received message \"%s\"" % result)
        return result

    def log(self, message):
        print("[WebSocket] : " + message)


###################---------OLD-----------################

#
#    def __init__(self, serverip):
#        self.serverip = serverip
#       self.log("WebSocket-Serveradresse " + serverip + " initialisiert.")
#        self.uri = "ws://"+serverip+":80"

#        wagen_server = websockets.serve(hello, "127.0.0.1", 8765)
#        asyncio.get_event_loop().run_until_complete(wagen_server)
#        asyncio.get_event_loop().run_forever()

#    def log(self, message):
#        print("[WebSocket] : " + message)

#    def sendMessage(self, message):
#        asyncio.get_event_loop().run_until_complete(
#            self.sendAsyncMessage(message))        

#    async def sendAsyncMessage(self, message):
#            async with websockets.connect(self.uri) as websocket:
#                await websocket.send(message)

#    def receiveMessage():
#        message = 



