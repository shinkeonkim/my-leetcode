class Solution:
    def minimumSum(self, num: int) -> int:
        l = sorted([*map(int, list(str(num)))])

        return (l[0] + l[1]) * 10 + l[2] + l[3]
