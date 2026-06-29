class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            diff_cnt = sum([s[i] != t[i] for i in range(len(s))])

            return diff_cnt == 1

        if len(s) + 1 == len(t):
            s, t = t, s

        if len(s) == len(t) + 1:
            diff_cnt = 0
            i = j = 0

            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    i += 1
                    diff_cnt += 1
                    continue

                i += 1
                j += 1

            diff_cnt += (len(s) - i)
            return diff_cnt == 1

        return False


