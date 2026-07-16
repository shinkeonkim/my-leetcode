class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        return sum([i ** k for i in [*map(int, str(n))]]) == n
