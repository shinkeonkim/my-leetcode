class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % i == 0 for i in map(int, list(str(num))))
