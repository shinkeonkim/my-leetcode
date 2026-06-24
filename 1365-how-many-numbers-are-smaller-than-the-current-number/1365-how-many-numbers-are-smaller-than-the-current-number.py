class Solution:  # naive
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            ret.append(sum([1 for j in nums if j < i]))
        return ret
