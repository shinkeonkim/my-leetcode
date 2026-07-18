from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.checkInInfo = {}
        self.timeSum = defaultdict(int)
        self.timeCount = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInInfo[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_tm = self.checkInInfo[id]
        self.checkInInfo[id] = ()
        key = (check_in_station, stationName)
        duration = t - check_in_tm

        self.timeSum[key] += duration
        self.timeCount[key] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        if self.timeCount[key] == 0:
            return 0

        return self.timeSum[key] / self.timeCount[key]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)