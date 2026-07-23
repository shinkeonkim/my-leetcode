# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float('inf')
        self.diff = float('inf')

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node):
            if self.diff > abs(target - node.val) or (self.diff == abs(target - node.val) and self.ans > node.val):
                self.diff = abs(target - node.val)
                self.ans = node.val

            if node.left is not None:
                dfs(node.left)

            if node.right is not None:
                dfs(node.right)

        dfs(root)

        return self.ans

