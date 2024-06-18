# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lis = []
        left_node = head

        for i in range(left - 1):
            left_node = left_node.next
        right_node = left_node

        for j in range(right - left + 1):
            lis.append(right_node.val)
            right_node = right_node.next

        right_ptr = right - left
        while left_node != right_node:
            left_node.val = lis[right_ptr]
            left_node = left_node.next
            right_ptr -= 1

        return head

