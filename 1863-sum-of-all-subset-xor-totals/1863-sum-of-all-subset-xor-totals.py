from functools import reduce
from itertools import combinations

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def all_xor(lst):
            return reduce(lambda acc, cur: acc ^ cur, lst)

        ans = 0
        for i in range(1, len(nums) + 1):
            ans += sum(all_xor(j) for j in combinations(nums, i))

        return ans
