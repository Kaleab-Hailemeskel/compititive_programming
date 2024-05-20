# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
        ##### My Implemetaion####
        # right = node.next
        # left = node
        # while right.next:
        #     left.val = right.val
        #     left = left.next
        #     right = right.next
        # left.val = right.val
        # left.next = None
