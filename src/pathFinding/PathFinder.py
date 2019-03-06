from Location import Location

class PathFinder(object):
    currentLocation = Location(0, 'A')

    def __init__(self, currentLocation):
        self.currentLocation = currentLocation

    def getDistanceToLoc(self, newLoc):
#	self.log("Aktuelle Position : %s. Zu fahrende Position: %s" % (self.currentLocation.getDist(), newLoc.getDist()))
        return (int(newLoc.getDist()) - int(self.currentLocation.getDist()))

    def updateLocation(self, distance):
        self.currentLocation.dist = self.currentLocation.dist + distance
    
    def setLocation(self, location):
        self.currentLocation.dist = location.dist

    def getLocation(self):
	return self.currentLocation

    def log(self, message):
        print("[Pathfinder] : %s" % message)
