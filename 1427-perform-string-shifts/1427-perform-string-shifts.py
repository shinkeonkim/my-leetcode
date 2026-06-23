class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sft = 0
        for i in range(len(shift)):
            diff = shift[i][1]
            if shift[i][0] == 0:  # left
                diff *= -1
            sft += diff

        if sft == 0:
            return s

        if sft > 0:
            sft %= len(s)

            return s[-sft:] + s[:-sft]

        if sft < 0:
            sft = (-sft) % len(s)

            return s[sft:] + s[:sft]
