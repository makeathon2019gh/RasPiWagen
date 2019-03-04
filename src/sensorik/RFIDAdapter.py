
#NDEF String for generating NDEF-File:
# ndeftool uri "http://google.de" save -k "serverconnect.ndef" print

import subprocess

fileString = None
created = False

class RFIDAdapter(object):
    def __init__(self):
        pass

    def generateNDEF(self, token):
        self.fileString = "serverconnect.ndef"
        subprocess.check_output(['ndeftool uri \"http://192.168.137.33:80/index.js?auth=%s\" save -k \"message.ndef\" print' % token])
        self.created = True
        
    def createConnection(self):
        response = subprocess.check_output(['nfc-emulate-forum-tag4 message.ndef'])
        response = response.lower()
        if 'rf transmission error' not in response:
            return
        else:
            self.createConnection()
            return
    


        

