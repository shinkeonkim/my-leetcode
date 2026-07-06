class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        crt = 0

        for i in gain:
            crt += i
            mx = max(mx, crt)

        return mx
