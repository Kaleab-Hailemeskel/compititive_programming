# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        while dummy_head:
            while dummy_head.next and dummy_head.next.val < x:
                dummy_head = dummy_head.next

            right = dummy_head.next
            while right and right.next and right.next.val >= x:
                right = right.next

            if right and right.next:
                head_swap = False
                if dummy_head.next == head:
                    head_swap  = True
                d = right.next
                b = dummy_head.next
                dummy_head.next = d
                right.next = right.next.next
                d.next = b
                if head_swap:
                    head = dummy_head.next


            dummy_head = dummy_head.next

        return head

