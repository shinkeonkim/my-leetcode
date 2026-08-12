class Solution:
    def convert(self, s: str, numRows: int) -> str:
        stack = [[] for _ in range(numRows)]

        direction = -1
        current = 0

        for i in range(len(s)):
            stack[current].append(s[i])

            if current == 0 or current == numRows - 1:
                direction *= -1

            current = (current + direction) % numRows

        return "".join(["".join(i) for i in stack])
