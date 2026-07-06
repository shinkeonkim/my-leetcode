class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def seperate(num):
            if num < 10:
                return [num]
            else:
                return seperate(num // 10) + [num % 10]

        ans = []

        for num in nums:
            ans.extend(seperate(num))

        return ans
