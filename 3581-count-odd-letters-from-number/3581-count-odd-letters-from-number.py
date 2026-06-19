from collections import Counter

class Solution:
    def countOddLetters(self, n: int) -> int:
        numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        count = Counter("".join([numbers[int(i)] for i in str(n)]))
        return sum([v % 2 for v in count.values()])
