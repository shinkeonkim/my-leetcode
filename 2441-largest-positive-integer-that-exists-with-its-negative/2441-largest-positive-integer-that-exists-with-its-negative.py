class Solution:
    def findMaxK(self, nums: List[int]) -> int:  # naive solution
        mx = -1

        for i in nums:
            if i > 0 and -i in nums:
                mx = max(mx, i)

        return mx
