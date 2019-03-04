
class PathFinder(object):
    currentLocation = Location()

    def __init__(self):
        pass

    def getDistanceToLoc(self, newLoc):
        return newLoc.dist - currentLocation.dist

    def updateLocation(self, distance):
        self.currentLocation.dist = self.currentLocation.dist + distance
    
    def setLocation(self, location):
        self.currentLocation.dist = location.dist