MOD = 10**9 + 7

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        dp = [-1] * 1100
        dp[0] = 1
        dp[2] = 1
        dp[4] = 2

        def dfs(leftPeople: int) -> int:
            if dp[leftPeople] != -1:
                return dp[leftPeople]

            dp[leftPeople] = 0
            k = leftPeople - 2
            for i in range(0, k + 1, 2):
                j = k - i

                dp[leftPeople] += dfs(i) * dfs(j)
                dp[leftPeople] %= MOD

            return dp[leftPeople]


        return dfs(numPeople)
