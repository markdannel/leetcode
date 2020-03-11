# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 说明: 叶子节点是指没有子节点的节点。
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, res, [], sum, 0)
        return res

    def dfs(self, root: TreeNode, res: List, load: List, sum: int, num: int) -> List[int]:
        if not root:
            return None
        load.append(root.val)
        if root.left:
            self.dfs(root.left, res, load, sum, num+root.val)
        if root.right:
            self.dfs(root.right, res, load, sum, num+root.val)
        if not root.left and not root.right:
            if sum==(num+root.val):
                res.append(load.copy())
        load.pop()