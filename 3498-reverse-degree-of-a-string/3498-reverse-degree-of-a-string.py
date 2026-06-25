class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_index = lambda ch : ord('z') - ord(ch) + 1
        return sum(rev_index(s[i]) * (i + 1) for i in range(len(s)))
