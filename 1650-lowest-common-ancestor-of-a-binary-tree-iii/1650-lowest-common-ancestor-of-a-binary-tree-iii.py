"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def findDepth(node, depth):
            if node.parent is None:
                return depth
            return findDepth(node.parent, depth + 1)

        p_depth = findDepth(p, 1)
        q_depth = findDepth(q, 1)

        while p != q:
            if p_depth == q_depth:
                p = p.parent
                q = q.parent
                p_depth -= 1
                q_depth -= 1
            elif p_depth > q_depth:
                p = p.parent
                p_depth -= 1
            else:
                q = q.parent
                q_depth -= 1

        return p
