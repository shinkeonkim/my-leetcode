"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def __init__(self):
        self.ans = 0

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def dfs(node, current_depth):
            depths = []

            if not node.children:
                return current_depth

            for child in node.children:
                depths.append(dfs(child, current_depth + 1))

            depths.sort()

            if len(depths) > 0:
                self.ans = max(self.ans, depths[-1])

            if len(depths) > 1:
                self.ans = max(self.ans, depths[-1] + depths[-2] - 2 * current_depth)

            return depths[-1]

        dfs(root, 0)
        return self.ans
