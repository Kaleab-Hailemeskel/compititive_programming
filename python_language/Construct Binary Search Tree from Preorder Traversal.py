# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(preorder[0])
        def insert(val):
            node = head
            while node:
                if val < node.val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(val)
                        break
                elif node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        for i in range(1, len(preorder)):
            insert(preorder[i])
        
        return head
                
        
