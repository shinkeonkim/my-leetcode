class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        last = lower - 1

        ans = []

        for i in nums:
            if last + 1 != i:
                ans.append([last + 1, i - 1])
            last = i

        if last != upper:
            ans.append([last + 1, upper])

        return ans
