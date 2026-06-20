# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        current = []

        def dfs(node, parent, direction):
            if node.left is None and node.right is None:
                current.append(node.val)

                if not parent:
                    return

                if direction == 'left':
                    parent.left = None
                else:
                    parent.right = None
                return

            if node.left:
                dfs(node.left, node, 'left')

            if node.right:
                dfs(node.right, node, 'right')


        while root and (root.left or root.right):
            dfs(root, None, "")
            ret.append(current[::])
            current = []

        ret.append([root.val])

        return ret
