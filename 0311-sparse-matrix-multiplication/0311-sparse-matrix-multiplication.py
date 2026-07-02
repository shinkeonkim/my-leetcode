class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        return [[sum(mat1[y][z] * mat2[z][x] for z in range(len(mat2))) for x in range(len(mat2[0]))] for y in range(len(mat1))]
