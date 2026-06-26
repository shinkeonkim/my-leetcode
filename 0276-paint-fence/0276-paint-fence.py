class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[0, 0, 0] for _ in range(max(n + 1, 3))]

        dp[1][1] = k
        dp[1][2] = 0
        dp[2][1] = k * (k - 1)
        dp[2][2] = k

        for i in range(2, n + 1):
            dp[i][1] = dp[i - 1][2] * (k - 1) + dp[i - 1][1] * (k - 1)
            dp[i][2] = dp[i - 1][1]

        return dp[n][1] + dp[n][2]
