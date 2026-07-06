class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        idx = num.find('6')
        num = [*num]

        if idx >= 0:
            num[idx] = '9'

        return int(''.join(num))
