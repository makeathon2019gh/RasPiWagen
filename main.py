import pigpio
from motorik import MotorAdapter
from sensorik import SensorAdapter

def main(object):
    pi = 0
    sensorAdapt = None
    motorAdapt = None
    if __name__ == "__main__":
        pi = pigpio.pi()
        sensorAdapt = SensorAdapter.SensorAdapter()
        motorAdapt = MotorAdapter.MotorAdapter(0,0,pi)

        pass

    