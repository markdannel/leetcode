# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = [], stack = [], nextstack = [], row = []
        stack.append(root)
        while not stack and not nextstack:
            if not stack:
                stack = nextstack
                nextstack = []
                res.append(row)
                row = []
            cur = stack.pop(0)
            if not cur:
                nextstack.append(cur.left)
                nextstack.append(cur.right)
                row.append(cur.val)
        return res