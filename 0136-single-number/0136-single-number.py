class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        i = 0

        while i < len(nums):
            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return nums[i]
            
            i += 2