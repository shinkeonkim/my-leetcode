"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""
from collections import Counter

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        mp = {}
        parent_cnt = Counter()

        for node in tree:
            key = node.val
            mp[key] = node
            parent_cnt[key] += 0

            for child in node.children:
                parent_cnt[child.val] += 1

        for k, v in parent_cnt.items():
            if v == 0:
                return mp[k]
