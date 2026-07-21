class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = []

        for i in range(1, len(arr)):
            diff.append(arr[i] - arr[i - 1])

        if diff[0] == diff[1] * 2:
            return arr[0] + diff[1]

        for i in range(1, len(diff)):
            if diff[i] == diff[0] * 2:
                return arr[i] + diff[0]
