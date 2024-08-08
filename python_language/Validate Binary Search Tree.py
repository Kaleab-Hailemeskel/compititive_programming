# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
################ MY SOLUTION  ###############
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        
        def inOrder(node):
            if not node: return
            if node.left:
                inOrder(node.left)
            arr.append(node.val)
            if node.right:
                inOrder(node.right)
        
        inOrder(root)
        print(arr)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True
############# EFFICENT SOLUTION###################
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))
                
        
