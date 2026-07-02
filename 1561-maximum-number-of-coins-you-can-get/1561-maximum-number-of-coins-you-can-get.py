class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        n = len(piles)
        ans = 0
        for i in range(n // 3):
            ans += piles[n - 2 * i - 2]

        return ans
