from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0

        for num in nums:
            ans += cnt[num + k] + cnt[num - k]
            cnt[num] -= 1

        return ans
