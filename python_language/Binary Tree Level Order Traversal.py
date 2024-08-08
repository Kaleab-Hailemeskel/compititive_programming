# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = [[root.val]]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
            if queue:
                res.append(level[:])
        return res
