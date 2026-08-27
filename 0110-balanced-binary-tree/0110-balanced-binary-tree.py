# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.f(root)[1]


    def f(self, node):
        if node is None:
            return 0, True
        
        left_height, is_left_balanced = self.f(node.left)
        right_height, is_right_balanced = self.f(node.right)
        
        height = max(left_height, right_height) + 1
        
        if abs(left_height - right_height) <= 1 and is_left_balanced and is_right_balanced:
            return height, True
        
        return height, False
