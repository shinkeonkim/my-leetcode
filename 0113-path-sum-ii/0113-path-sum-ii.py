# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = []
        self.current_nodes = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.tracker(root, 0, targetSum)

        return self.answer
    

    def isLeaf(self, node: Optional[TreeNode]) -> bool:
        return node is not None and node.left is None and node.right is None

    def tracker(self, node: Optional[TreeNode], currentSum: int, targetSum: int) -> bool:
        if node is None:
            return False
    
        currentSum += node.val
        self.current_nodes.append(node.val)

        if self.isLeaf(node):
            if currentSum == targetSum:
                self.answer.append(self.current_nodes[::])
            
            self.current_nodes.pop()
            return

        self.tracker(node.left, currentSum, targetSum)
        self.tracker(node.right, currentSum, targetSum)
        self.current_nodes.pop()
