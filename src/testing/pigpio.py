
class pigpio(object):

    def __init__(self):
        print(" PiGpio wurde initialisiert. ")

        pass

    def pi(self):
        self.log(" Ein Pi-Objekt wurde angefordert.")
        return pi()

    def log(self, nachricht):
        print("[pigpio] :" + nachricht)


class pi(object):

    def __init__(self):
        
        pass
