# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.getDepth(root) == -1:
            return False
        return True

    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lo = self.getDepth(root.left)
        hi = self.getDepth(root.right)
        if lo==-1 or hi==-1:
            return -1
        if abs(hi-lo) > 1:
            return -1
        return max(lo, hi)+1
