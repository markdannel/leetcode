# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
# 示例 1:
# 输入:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 注意：
# 节点值的范围在32位有符号整数范围内。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        res, stack = [], [(0,root)]
        sum, num, count = 0, 0, 0
        while stack:
            d,cur = stack.pop(0)
            if d == num:
                count +=1
                sum += cur.val
            else:
                res.append(sum/count)
                sum = cur.val
                count = 1
                num = d
            if cur.left:
                stack.append((d+1,cur.left))
            if cur.right:
                stack.append((d+1,cur.right))
        res.append(sum/count)
        return res

    # 另一个思路:将一整层当做单位遍历
    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        res = []
        layer = [root]
        while layer:
            res.append(sum(node.val for node in layer) / len(layer))
            temp_layer = []
            while layer:
                cur = layer.pop(0)
                if cur.left:
                    temp_layer.append(cur.left)
                if cur.right:
                    temp_layer.append(cur.right)
            layer = temp_layer
        return res

