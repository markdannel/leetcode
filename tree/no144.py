# 给定一个二叉树，返回它的 前序 遍历。
#  示例:
# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root.val]
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res
        
        # 非递归
        # res, stack = [], [root]
        # while stack:
        #     node = stack.pop(0)
        #     res.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
            
