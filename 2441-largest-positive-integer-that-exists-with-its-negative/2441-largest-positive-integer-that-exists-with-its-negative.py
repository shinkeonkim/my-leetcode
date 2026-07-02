from collections import defaultdict

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        d = defaultdict(bool)
        ans = -1

        for i in nums:
            if i < 0:
                d[i] = True

            if i > 0 and d[-i]:
                ans = i

        return ans
