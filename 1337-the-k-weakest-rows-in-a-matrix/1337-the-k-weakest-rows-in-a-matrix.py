class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[1] for i in sorted([[sum(mat[i]), i] for i in range(len(mat))])][:k]
