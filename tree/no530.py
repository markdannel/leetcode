# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
# 示例：
# 输入：
# 
#    1
#     \
#      3
#     /
#    2
# 输出：
# 1
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 提示：
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        def dfs(root):
            if not root:
                return []
            return dfs(root.left)+[root.val]+dfs(root.right)
        
        if not root:
            return 0
        res = dfs(root)
        minn = 99999999
        for i in range(1, len(res)):
            minn = min(minn, res[i]-res[i-1])
            print(i, res[i])
        return minn

#[236,104,701,null,227,null,911] -> 9
# root = TreeNode(236)
# root.left = TreeNode(104)
# root.right = TreeNode(701)
# root.left.right = TreeNode(227)
# root.right.right = TreeNode(911)
root = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(3)
s = Solution()
r = s.getMinimumDifference(root)
print(r)