class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            ret = 0
            while n > 0:
                ret += n % 10
                n //= 10
            return ret

        sm1 = sum(nums)
        sm2 = sum([*map(digit_sum, nums)])

        return abs(sm1 - sm2)
