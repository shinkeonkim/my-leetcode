class Solution:
    def interpret(self, command: str) -> str:
        stk = []

        for i in command:
            stk.append(i)

            if len(stk) >= 2 and stk[-2] == '(' and stk[-1] == ')':
                stk.pop()
                stk.pop()
                stk.append('o')

            if len(stk) >= 4 and "".join(stk[-4:]) == '(al)':
                stk = stk[:-4]
                stk.extend(['a', 'l'])

        return "".join(stk)
