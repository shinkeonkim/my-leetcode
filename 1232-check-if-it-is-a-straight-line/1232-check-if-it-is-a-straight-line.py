class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        diff0 = coordinates[1][0] - coordinates[0][0]
        diff1 = coordinates[1][1] - coordinates[0][1]

        print(coordinates)

        if all(coordinates[0][0] == i[0] for i in coordinates):
            return True

        if all(coordinates[0][1] == i[1] for i in coordinates):
            return True

        for i in range(2, len(coordinates)):
            if diff1 * (coordinates[i][0] - coordinates[i - 1][0]) != diff0 * (coordinates[i][1] - coordinates[i - 1][1]):
                return False

        return True
