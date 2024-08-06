class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        ans_root = TreeNode()
        if not(root1 or root2):
            return None

        def preOrder(node1, node2, ans):
            ans_val = 0
            node1_r = node1_l = node2_r = node2_l = None
            if node1: 
                ans_val += node1.val
                node1_r = node1.right
                node1_l = node1.left
            if node2:
                node2_r = node2.right
                node2_l = node2.left
                ans_val += node2.val
            ans.val = ans_val
            if node1_l or node2_l:
                ans.left = TreeNode()
                preOrder(node1_l, node2_l, ans.left)
            if node2_r or node1_r:
                ans.right = TreeNode()
                preOrder(node1_r, node2_r, ans.right)
          
        preOrder(root1, root2, ans_root)
        return ans_root
