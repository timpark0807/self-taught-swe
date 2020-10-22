class Route:
    def __init__(self):
        self.time = 0.0
        self.trips = 0.0
        
    def addTrip(self, time):
        self.time += time 
        self.trips += 1.0
        
    def getAverage(self):
        return self.time / self.trips 
    

class UndergroundSystem(object):

    def __init__(self):
        self.routes = {}  # route : average time 
        self.checked = {}  # id : [startStation, startTime]
        
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checked[id] = [stationName, t] 
         
    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.checked[id] 
        
        if (startStation, stationName) not in self.routes:
            self.routes[(startStation, stationName)] = Route() 
        
        route = self.routes[(startStation, stationName)]
        route.addTrip(t-startTime) 

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return self.routes[(startStation, endStation)].getAverage() 
    


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
