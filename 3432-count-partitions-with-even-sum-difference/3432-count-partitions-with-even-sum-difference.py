class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        sm = sum(nums)
        part1 = 0
        ans = 0

        for i in nums[:-1]:
            part1 += i
            part2 = sm - part1

            if abs(part1 - part2) % 2 == 0:
                ans += 1

        return ans
