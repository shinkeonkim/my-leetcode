class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0

        for i in range(n):
            s += mat[i][i]
            if n - 1 != i * 2:
                s += mat[n - i - 1][i]

        return s
