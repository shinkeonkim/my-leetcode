# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def findNode(original_node, cloned_node, target_node):
            if original_node.val == target_node.val:
                return cloned_node

            if original_node.left is not None:
                result = findNode(original_node.left, cloned_node.left, target)

                if result is not None:
                    return result

            if original_node.right is not None:
                result = findNode(original_node.right, cloned_node.right, target)

                if result is not None:
                    return result

            return None

        return findNode(original, cloned, target)
