class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        st = set(nums)
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] != diff:
                    continue

                if 2 * nums[j] - nums[i] in st:
                    ans += 1

        return ans
