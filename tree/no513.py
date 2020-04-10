# 给定一个二叉树，在树的最后一行找到最左边的值。
# 示例 1:
# 输入:
#     2
#    / \
#   1   3
# 输出:
# 1
# 示例 2:
# 输入:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# 输出:
# 7
# 注意: 您可以假设树（即给定的根节点）不为 NULL。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        res = [(0, root)]
        bottom_left, max_deep = 0, -1
        #deep,cur = 0, root
        while res:
            deep,cur = res.pop(0)
            if deep > max_deep:
                max_deep = deep
                bottom_left = cur.val
            if cur.left:
                res.append((deep+1, cur.left))
            if cur.right:
                res.append((deep+1, cur.right))
        return bottom_left
        
        
        
        
        
        
        
        
        
        