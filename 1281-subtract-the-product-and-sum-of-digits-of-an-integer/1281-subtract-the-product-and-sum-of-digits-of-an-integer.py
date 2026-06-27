class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        d = [*map(int, str(abs(n)))]

        pd = 1
        sm = sum(d)
        for i in d:
            pd *= i

        return pd - sm
