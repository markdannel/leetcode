# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
# 示例 1：
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# 下面是两个重复的子树：
#       2
#      /
#     4
# 和
#     4
# 因此，你需要以列表的形式返回上述重复子树的根结点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        counter = collections.Counter()
        ans = []
        def dfs(node):
            if not node:
                return "#"
            r = "{},{},{}".format(node.val, dfs(node.left), dfs(node.right))
            counter[r] += 1
            if counter[r] == 2:
                ans.append(node)
            return r
        dfs(root)
        return ans