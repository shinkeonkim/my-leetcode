class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dis(a, b):
            return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

        return sum(dis(points[i - 1], points[i]) for i in range(1, len(points)))
