# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1,null,2,3] => [1,3,2]
class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res
    
    def inorderTraversal2(self, root):
        stack,res=[],[]
        cur = root
        while stack and cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res