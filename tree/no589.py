# 给定一个 N 叉树，返回其节点值的前序遍历。
# 例如，给定一个 3叉树 :
#            1
#          / | \
#         3  2  4
#        / \     
#       5   6    
# 返回其前序遍历: [1,3,5,6,2,4]。
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 递归
        # if not root:
        #     return []
        # res = [root.val]
        # for node in root.children:
        #     res += self.preorder(node)
        # return res
        # N叉树非递归时，取栈第0个就是层序遍历，取栈最后一个就是深度遍历
        if not root:
            return []
        stack, res = [root],[]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for node in cur.children[::-1]: # 栈的性质
                stack.append(node)
        return res