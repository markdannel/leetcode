# [-10,9,20,null,null,15,7]
class Solution:
    maxSum = 0
    curSum = 0
    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.maxSum

    def dfs(self, root):
        if not root:
            return 0
        
        self.curSum += self.dfs(root.left)
        self.curSum += self.dfs(root.right)
        self.curSum += root.val
        print(root.val, self.curSum)
        if self.curSum > self.maxSum:
            self.maxSum = self.curSum
        return self.curSum