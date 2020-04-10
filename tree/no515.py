# 您需要在二叉树的每一行中找到最大的值。
# 示例：
# 输入: 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 输出: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(0, root)]
        while stack:
            deep, cur = stack.pop(0)
            if len(res) == deep:
                res.append(cur.val)
            if res[deep] < cur.val:
                res[deep] = cur.val
            if cur.left:
                stack.append((deep+1, cur.left))
            if cur.right:
                stack.append((deep+1, cur.right))
        return res
