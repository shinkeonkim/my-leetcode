from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {i: i for i in arr1}
        for i in range(len(arr2)):
            d[arr2[i]] = -len(arr2) - 1 + i

        arr1.sort(key = lambda t: d[t])

        return arr1
