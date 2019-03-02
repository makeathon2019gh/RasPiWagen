import websockets
import asyncio

class WebSocketAdapter(object):
    
    serverip = "127.0.0.1"
    uri = "ws://"+serverip+":8765"

    def __init__(self, serverip):
        self.serverip = serverip
        self.log("WebSocket-Serveradresse " + serverip + " initialisiert.")
        self.uri = "ws://"+serverip+":8765"

        wagen_server = websockets.serve(hello, "127.0.0.1", 8765)
        asyncio.get_event_loop().run_until_complete(wagen_server)
        asyncio.get_event_loop().run_forever()

    def log(self, message):
        print("[WebSocket] : " + message)

    def sendMessage(self, message):
        asyncio.get_event_loop().run_until_complete(
            self.sendAsyncMessage(message))        

    async def sendAsyncMessage(self, message):
            async with websockets.connect(self.uri) as websocket:
                await websocket.send(message)

    def receiveMessage():
        message = 



