class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda t: (-t[1]))

        currentSize = truckSize
        ans = 0

        for count, units in boxTypes:
            availableCount = min(count, currentSize)
            currentSize -= availableCount
            ans += availableCount * units

        return ans
