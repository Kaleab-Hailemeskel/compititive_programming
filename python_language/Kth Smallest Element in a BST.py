# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left = right = 0
        if root.left:
            left = self.kthSmallest(root.left, k)
        self.count += 1
        if self.count == k:
            return root.val
        if root.right:
            right = self.kthSmallest(root.right, k)
        return right or left
        
        
        
        
