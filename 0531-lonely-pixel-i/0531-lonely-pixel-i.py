from collections import Counter
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_cnt = Counter()
        col_cnt = Counter()

        n = len(picture)
        m = len(picture[0])

        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B':
                    row_cnt[i] += 1
                    col_cnt[j] += 1

        ans = 0
        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B' and row_cnt[i] == col_cnt[j] == 1:
                    ans += 1

        return ans
