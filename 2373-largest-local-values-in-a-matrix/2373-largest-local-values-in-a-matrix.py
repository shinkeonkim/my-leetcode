class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(grid)
        dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dx = [1, 0, -1, 1, 0, -1, 1, 0, -1]

        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                mx = -1
                for d in range(9):
                    ny = i + dy[d]
                    nx = j + dx[d]

                    mx = max(mx, grid[ny][nx])
                row.append(mx)

            ans.append(row)
            row = []

        return ans
