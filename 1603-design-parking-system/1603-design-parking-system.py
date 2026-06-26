class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capcities = [0, big, medium, small]
        self.count = [0, 0, 0, 0]

    def addCar(self, carType: int) -> bool:
        if self.count[carType] + 1 <= self.capcities[carType]:
            self.count[carType] += 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
