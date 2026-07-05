class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(2, len(s) + 1):
            if len(s) % i > 0:
                continue

            ln = len(s) // i

            if s == s[:ln] * i:
                return True

        return False
