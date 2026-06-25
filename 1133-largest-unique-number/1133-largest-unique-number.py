from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        mx = -1

        for k, v in count.items():
            if v >= 2:
                continue

            mx = max(k, mx)

        return mx
