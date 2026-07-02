class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        n = len(mat1)
        m = len(mat2)
        k = len(mat2[0])

        ret = []
        for y in range(n):
            row = []
            for x in range(k):
                row.append(sum(mat1[y][z] * mat2[z][x] for z in range(m)))

            ret.append(row)

        return ret
