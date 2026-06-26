INF = float('inf')

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = len(costs[0])
        dp = [[INF] *  m for _ in range(n)]

        for j in range(m):
            dp[0][j] = costs[0][j]

        for i in range(1, n):
            for j in range(m):
                for prev_j in range(m):
                    if j == prev_j:
                        continue

                    dp[i][j] = min(dp[i][j], dp[i - 1][prev_j] + costs[i][j])

        return min(dp[n - 1])
