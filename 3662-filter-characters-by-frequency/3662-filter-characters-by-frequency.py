class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        s2 = []

        for i in s:
            if s.count(i) < k:
                s2.append(i)

        return "".join(s2)
