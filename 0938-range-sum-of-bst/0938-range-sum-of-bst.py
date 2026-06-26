# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ret = 0
        if low <= root.val <= high:
            ret += root.val

        left = root.left
        right = root.right

        if left is not None and low < root.val:
            ret += self.rangeSumBST(left, low, high)

        if right is not None and root.val < high:
            ret += self.rangeSumBST(right, low, high)

        return ret
