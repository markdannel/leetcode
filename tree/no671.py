# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 示例 1:
# 输入: 
#     2
#    / \
#   2   5
#      / \
#     5   7
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 示例 2:
# 输入: 
#     2
#    / \
#   2   2
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        minn, minn2 = root.val, root.val
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if cur.val > minn:
                if minn2 > cur.val or minn == minn2:
                    minn2 = cur.val
                else:
                    continue
            if cur.left:
                stack.append(cur.left)
                stack.append(cur.right)
        return minn2

s = Solution()
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(6)
r = s.findSecondMinimumValue(root)
print(r)
