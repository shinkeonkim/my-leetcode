# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        leading = 0
        start = None
        prev = None

        while l1 is not None and l2 is not None:
            current_val = (l1.val + l2.val + leading) % 10
            leading = (l1.val + l2.val + leading) // 10

            current = ListNode(current_val, None)

            if prev is not None:
                prev.next = current
            else:
                start = current

            prev = current
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            current_val = (l1.val + leading) % 10
            leading = (l1.val + leading) // 10

            current = ListNode(current_val, None)

            if prev is not None:
                prev.next = current
            else:
                start = current

            prev = current
            l1 = l1.next


        while l2 is not None:
            current_val = (l2.val + leading) % 10
            leading = (l2.val + leading) // 10

            current = ListNode(current_val, None)

            if prev is not None:
                prev.next = current
            else:
                start = current

            prev = current
            l2 = l2.next

        if leading > 0:
            current = ListNode(leading, None)
            prev.next = current

        return start
