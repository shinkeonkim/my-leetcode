class Solution:
    def numberOfMatches(self, n: int) -> int:
        ret = 0
        team = n

        while team > 1:
            if team % 2 == 0:
                ret += team // 2
                team //= 2
            else:
                ret += (team - 1) // 2
                team = (team - 1) // 2 + 1

        return ret
