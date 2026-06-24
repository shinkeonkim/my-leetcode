class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = 0
        splitted = []
        split_start = 0

        for i in range(len(s)):
            if s[i] == '(':
                stk += 1
            else:
                stk -= 1

            if stk == 0:
                splitted.append(s[split_start:i + 1])
                split_start = i + 1

        return "".join(i[1:-1] for i in splitted)
