# 在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：
# 行数 m 应当等于给定二叉树的高度。
# 列数 n 应当总是奇数。
# 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分
# （左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。
# 即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。
# 然而，如果两个子树都为空则不需要为它们留出任何空间。
# 每个未使用的空间应包含一个空的字符串""。
# 使用相同的规则输出子树。
# 示例 1:
# 输入:
#      1
#     /
#    2
# 输出:
# [["", "1", ""],
#  ["2", "", ""]]
# 示例 2:
# 输入:
#      1
#     / \
#    2   3
#     \
#      4
# 输出:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# 示例 3:
# 输入:
#       1
#      / \
#     2   5
#    / 
#   3 
#  / 
# 4 
# 输出:
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# 注意: 二叉树的高度在范围 [1, 10] 中。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root: TreeNode):
        depth = self.findDepth(root)
        m,n = depth,2**depth-1
        res=[[""] * n for i in range(m)]
        #[node,depth,base,offset]
        stack = [(root,0, 0, int(n/2))]
        while stack:
            node,d,base,ofs = stack.pop(0)
            res[d][base+ofs] = str(node.val)
            mid = int((abs(ofs)+1)/2)
            if node.left:
                stack.append((node.left, d+1, base+ofs, -1*mid))
            if node.right:
                stack.append((node.right, d+1, base+ofs, mid))
        return res

    def findDepth(self, root):
        if not root:
            return 0
        return 1+max(self.findDepth(root.left), self.findDepth(root.right))

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
nums = s.printTree(root)
print(nums)