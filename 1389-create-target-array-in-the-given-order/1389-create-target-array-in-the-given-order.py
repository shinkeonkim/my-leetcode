class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            num = nums[i]
            idx = index[i]

            ret = ret[:idx] + [num] + ret[idx:]

        return ret
