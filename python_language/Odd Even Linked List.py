# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        first = head

        while first and count < 3:
            count += 1
            first = first.next
        if count < 3:
            return head
        
        first = head
        hold = ListNode(0)
        dummy = hold
        while first and first.next and first.next.next:
            hold.next = ListNode(first.val)
            first = first.next.next
            hold = hold.next
        
        if first:
            hold.next = ListNode(first.val)
            hold = hold.next 
            
        first = head.next
        while first and first.next and first.next.next:
            hold.next = ListNode(first.val)
            first = first.next.next
            hold = hold.next
        
        if first:
            hold.next = ListNode(first.val)
            hold = hold.next 
        
        return dummy.next
            
