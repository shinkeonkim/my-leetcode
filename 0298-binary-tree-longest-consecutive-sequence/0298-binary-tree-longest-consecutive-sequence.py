# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prev_val, cnt):
            if node is None:
                return 0

            ret = cnt
            if prev_val is None:
                ret = 1
            else:
                if prev_val + 1 == node.val:
                    ret = cnt + 1
                else:
                    ret = 1

            self.ans = max(self.ans, ret)

            if node.left is not None:
                dfs(node.left, node.val, ret)

            if node.right is not None:
                dfs(node.right, node.val, ret)

        dfs(root, None, 0)

        return self.ans
