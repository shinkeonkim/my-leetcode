class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = [nums[0]]

        for i in nums[1:]:
            acc.append(acc[-1] + i)

        return acc
