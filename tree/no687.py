# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
# 注意：两个节点之间的路径长度由它们之间的边数表示。
# 示例 1:
# 输入:
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# 输出:
# 2
# 示例 2:
# 输入:
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# 输出:
# 2
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# [1,null,1,1,1,1,1,1]
class Solution:
    maxx = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root, -100)
        return self.maxx

    def dfs(self, root, val):
        if not root:
            return 0
        le = self.dfs(root.left, root.val)
        ri = self.dfs(root.right, root.val)
        self.maxx = max(self.maxx, le+ri)
        if root.val == val:
            return max(le, ri) + 1
        else:
            return 0
# [1,null,1,1,1,1,1,1]
s = Solution()
root = TreeNode(1)
# root.left = TreeNode(4)
root.right = TreeNode(1)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)
root.right.right.left = TreeNode(1)

p = s.longestUnivaluePath(root)
print(p)