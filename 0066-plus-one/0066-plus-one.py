class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ret = []

        for i in digits[::-1]:
            crt = carry + i

            ret.append(crt % 10)
            carry = crt // 10

        if carry > 0:
            ret.append(carry)

        return ret[::-1]
