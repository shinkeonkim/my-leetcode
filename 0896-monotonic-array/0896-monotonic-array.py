class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if all(nums[i - 1] <= nums[i] for i in range(1, len(nums))):
            return True

        if all(nums[i - 1] >= nums[i] for i in range(1, len(nums))):
            return True

        return False
