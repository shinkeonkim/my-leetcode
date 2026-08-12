# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        isFirst = True
        prev = None

        while current is not None:
            nxt = current.next
            nnxt = None

            if nxt is None:
                break

            nnxt = nxt.next
            current.next = nnxt
            nxt.next = current

            if prev:
                prev.next = nxt

            prev = current

            if isFirst:
                head = nxt
                isFirst = False

            current = nnxt

        return head
