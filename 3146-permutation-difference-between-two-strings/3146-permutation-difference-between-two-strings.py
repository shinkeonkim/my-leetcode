class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {t[i]: i for i in range(len(t))}

        return sum(abs(i - d[s[i]]) for i in range(len(s)))
