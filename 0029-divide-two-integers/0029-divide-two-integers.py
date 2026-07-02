MAX_INT = 2 ** 31 - 1
MIN_INT = - 2 ** 31
class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if is_negative:
            quotient *= -1

        return max(MIN_INT, min(MAX_INT, quotient))
