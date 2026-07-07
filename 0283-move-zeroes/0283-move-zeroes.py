class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ret = []
        cnt = 0

        for i in nums:
            if i == 0:
                cnt += 1
            else:
                ret.append(i)
        ret.extend([0] * cnt)

        nums[:] = ret
