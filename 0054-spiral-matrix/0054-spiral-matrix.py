from collections import defaultdict

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        chk = defaultdict(bool)
        d = 0

        n = len(matrix)
        m = len(matrix[0])
        y = 0
        x = 0
        ans = []

        for _ in range(n * m):
            ans.append(matrix[y][x])
            chk[(y, x)] = True

            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or nx < 0 or ny >= n or nx >= m or chk[(ny, nx)]:
                d = (d + 1) % 4
                ny = y + dy[d]
                nx = x + dx[d]

            y, x = ny, nx

        return ans
