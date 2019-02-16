import pigpio
 

class MotorAdapter(object):
    pinAntrieb = 0
    pinSteuerung = 0
    pi = None

    def powerOn(self):
        pass
    def powerOff(self):
        pass
    def __init__(self, pinAntrieb, pinSteuerung, pi):
        self.pinAntrieb = pinAntrieb
        self.pinSteuerung = pinSteuerung
        self.pi = pi

        