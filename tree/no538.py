# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
# 例如：
# 输入: 原始二叉搜索树:
#               5
#             /   \
#            2     13
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13
# 注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    num = 0;
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        root.val = root.val + self.num
        self.num = root.val
        self.convertBST(root.left)
        return root

# [2,0,3,-4,1]
# [5,6,3,2,1]
# 预期结果
# [5,6,3,2,6]
root = TreeNode(2)
root.right = TreeNode(3)
root.left = TreeNode(0)
root.left.left = TreeNode(-4)
root.left.right = TreeNode(1)
s = Solution()
res = s.convertBST(root)
print(res.val)
print(res.left.left.val)
print(res.left.right.val)