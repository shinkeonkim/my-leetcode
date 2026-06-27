class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = sorted(edges[0])
        c, d = sorted(edges[1])

        if a == c:
            return a

        return b
