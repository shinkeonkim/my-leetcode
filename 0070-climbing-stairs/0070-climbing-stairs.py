dp = [0, 1, 2] + [-1] * 100

class Solution:
    def climbStairs(self, n: int) -> int:
        if dp[n] > 0:
            return dp[n]
        
        dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return dp[n]
