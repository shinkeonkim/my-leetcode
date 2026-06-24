class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda t:t[1])
        prev = intervals[0]

        for i in range(1, len(intervals)):
            crt = intervals[i]

            if prev[1] <= crt[0]:
                prev = crt
                continue

            return False

        return True
