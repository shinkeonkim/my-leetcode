class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = 0
        ans = 0

        for i in s:
            if i == 'R':
                r += 1
            if i == 'L':
                l += 1

            if r == l and l != 0:
                ans += 1

        return ans
