# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, node: Optional[TreeNode]) -> bool:
        return node is not None and node.left is None and node.right is None

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.tracker(root, 0, targetSum)

    def tracker(self, node: Optional[TreeNode], currentSum: int, targetSum: int) -> bool:
        if node is None:
            return False
    
        currentSum += node.val

        if self.isLeaf(node):
            return currentSum == targetSum
        

        leftResult = self.tracker(node.left, currentSum, targetSum)
        rightResult = self.tracker(node.right, currentSum, targetSum)

        return leftResult or rightResult
