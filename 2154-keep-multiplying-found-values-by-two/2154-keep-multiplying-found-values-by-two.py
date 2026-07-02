class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        target = original

        for i in nums:
            if i == target:
                target *= 2

        return target
