class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 1:
            return num

        if num % 2 == 0:
            return self.numberOfSteps(num // 2) + 1

        return self.numberOfSteps(num - 1) + 1
