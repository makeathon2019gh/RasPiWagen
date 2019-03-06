

class Location(object):

    dist = 0
    knoten = "A"

    def __init__(self, dist, knoten):
        self.dist = dist
        self.knoten = knoten

    def getDist(self):
	return self.dist
