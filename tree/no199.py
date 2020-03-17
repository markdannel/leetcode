# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 示例:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [(0,root)]
        res = []
        while stack:
            p, cur = stack.pop(0)
            if cur.left:
                stack.append((p+1,cur.left))
            if cur.right:
                stack.append((p+1,cur.right))
            if len(res)==p:
                res.append(cur.val)
            else:
                res[p]=cur.val
        return res