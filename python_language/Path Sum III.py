# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, sum_):
            if not node: 
                return 0
            sum_ += node.val
            return int(sum_ == targetSum) + dfs(node.right, sum_) + dfs(node.left, sum_)
            
        
        def left_right(node):
            if not node: return 0
            return dfs(node, 0) + left_right(node.left) + left_right(node.right)
        
        
        return left_right(root)
