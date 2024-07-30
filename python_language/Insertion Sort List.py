# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val < cur.val:
                while pre.next and pre.next.val < cur.next.val:
                    pre = pre.next
                temp = pre.next
                pre.next = cur.next
                cur.next = cur.next.next
                pre.next.next = temp
                pre = dummy
            else:
                cur = cur.next
        return dummy.next
