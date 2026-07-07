class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if s == "":
            return 0

        ret = 0
        idx = 0
        is_minus = False
        if s[0] == '-':
            is_minus = True
            idx += 1
        elif s[0] == '+':
            idx += 1

        while idx < len(s):
            i = s[idx]
            idx += 1

            if ord('0') <= ord(i) <= ord('9'):
                ret *= 10
                ret += ord(i) - ord('0')
            else:
                break

        if is_minus:
            ret *= -1

        return min(max(ret, -2 ** 31), 2 ** 31 - 1)
