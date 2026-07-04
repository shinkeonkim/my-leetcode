# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        prev = None

        if list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                start = list1
                list1 = list1.next
            else:
                start = list2
                list2 = list2.next
        elif list1 is not None:
            start = list1
            list1 = list1.next
        elif list2 is not None:
            start = list2
            list2 = list2.next
        else:
            return None

        prev = start

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        while list1 is not None:
            prev.next = list1
            prev = list1
            list1 = list1.next

        while list2 is not None:
            prev.next = list2
            prev = list2
            list2 = list2.next

        return start
