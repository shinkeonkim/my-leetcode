from collections import Counter
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = Counter()
        node = head
        while 1:
            counter[node.val] += 1

            if node.next is None:
                break

            node = node.next

        mx = max(counter.keys())

        head = None
        prev = None
        for i in range(1, mx + 1):
            if counter[i] == 0:
                continue

            new_node = ListNode(counter[i])
            if prev is not None:
                prev.next = new_node

            if head is None:
                head = new_node

            prev = new_node

        return head
