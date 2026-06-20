class Solution:
    def confusingNumber(self, n: int) -> bool:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        for i in str(n):
            if i in '23457':
                return False

        return "".join([d[i] for i in str(n)[::-1]]) != str(n)
