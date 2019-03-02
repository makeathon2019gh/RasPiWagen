
from testing import pigpio
from motorik import MotorAdapter
from sensorik import SensorAdapter
from network import WebSocketAdapter

pi = 0
pigpi = pigpio()
sensorAdapt = None
motorAdapt = None
webSocketAdapt = None 

if __name__ == "__main__":

        print("--------------- Der Einkaufswagen wurde gestartet ---------------")

        pi = pigpi.pi()
        sensorAdapt = SensorAdapter.SensorAdapter()
        motorAdapt = MotorAdapter.MotorAdapter(0,0,pi)
        webSocketAdapt = WebSocketAdapter.WebSocketAdapter("192.168.178.20")
        pass

    