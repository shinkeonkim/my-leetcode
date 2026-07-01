from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = sorted(Counter(arr).items())
        ans = 0

        for i in range(1, len(count)):
            if count[i - 1][0] + 1 == count[i][0]:
                ans += count[i - 1][1]

        return ans
