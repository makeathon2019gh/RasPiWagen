from Location import Location

class PathFinder(object):
    currentLocation = Location(0, 'A')

    def __init__(self):
        pass

    def getDistanceToLoc(self, newLoc):
        return newLoc.dist - self.currentLocation.dist

    def updateLocation(self, distance):
        self.currentLocation.dist = self.currentLocation.dist + distance
    
    def setLocation(self, location):
        self.currentLocation.dist = location.dist

    def log(self, message):
        print("[Pathfinder] : %s" % message)
