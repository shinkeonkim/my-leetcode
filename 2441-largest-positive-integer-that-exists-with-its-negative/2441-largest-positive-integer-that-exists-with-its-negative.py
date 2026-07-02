class Solution:
    def findMaxK(self, nums: List[int]) -> int:  # naive solution
        nums.sort()
        d = {}
        ans = -1

        for i in nums:
            if i < 0:
                d[i] = 1

            if i > 0 and -i in d:
                ans = i

        return ans
