# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
# 示例：
#     7
#    / \
#   3  15
#     /  \
#    9    20
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = self.dfs(root)

    def dfs(self, root: TreeNode) -> List:
        if not root:
            return []
        res = []
        res += dfs(root.left)
        res.append(root.val)
        res += dfs(root.right)
        return res

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.data:
            return None
        return self.data.pop(0)


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.data:
            return False
        return  True



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()