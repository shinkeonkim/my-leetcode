class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(sum(i) for i in tasks)
