"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # def deep_copy(copied_node):
        #     copying_node.val = copied_node.val

        #     if copied_node.children is None:
        #         return

        #     copying_node.children = [
        #         dfs(copied_children_node, Node())
                
        #     ]

        copying_root = deepcopy(root)

        return copying_root
