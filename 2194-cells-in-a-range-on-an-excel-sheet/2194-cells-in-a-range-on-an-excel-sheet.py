class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        def str_to_axis(s):
            return (ord(s[0]), int(s[1]))

        from_axis, to_axis = map(str_to_axis, s.split(":"))
        ans = []

        for row in range(from_axis[0], to_axis[0] + 1):
            for col in range(from_axis[1], to_axis[1] + 1):
                ans.append(chr(row) + str(col))

        return ans

