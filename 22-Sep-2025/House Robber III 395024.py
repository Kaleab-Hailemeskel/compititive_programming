# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def recur(node):
            if not node:
                return 0
            
            if node not in dp:
                left_child = node.left
                right_child = node.right
                llgc = None
                lrgc = None
                rlgc = None
                rrgc = None
                sum_grand_child = 0
                # let's initialize the grand children
                if left_child:
                    llgc = left_child.left
                    lrgc = left_child.right

                if right_child:
                    rlgc = right_child.left
                    rrgc = right_child.right
                sum_grand_child = recur(llgc) + recur(lrgc) + recur(rlgc) + recur(rrgc)
                dp[node] = max(recur(left_child) + recur(right_child), node.val + sum_grand_child)
            return dp[node]
        return recur(root)