class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        mn = nums[0]
        mx = nums[-1]

        return [i for i in range(mn, mx + 1) if i not in nums]
            