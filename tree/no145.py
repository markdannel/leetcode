# 给定一个二叉树，返回它的 后序 遍历。
# 示例:
# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # res = []
        # res += self.postorderTraversal(root.left)
        # res += self.postorderTraversal(root.right)
        # res.append(root.val)
        # return res

        #非递归
        res, stack = [], [root]
        cur, last = root, root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack[-1]
                if not cur.right or last==cur:
                    res.append(cur.val)
                    stack.pop()
                    last = cur
                    cur = None
                else:
                    cur = cur.right
        return res
