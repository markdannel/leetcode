# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例:

# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

class Solution:
    def minPathSum(self, grid) -> int:
        if len(grid) < 1: return 0
        m,n = len(grid),len(grid[0])
        dp = [[100000 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
        for i in range(m-2,-1,-1):
            dp[i][n-1] = dp[i+1][n-1] + grid[i][n-1]
        for i in range(n-2,-1,-1):
            dp[m-1][i] = dp[m-1][i+1] + grid[m-1][i]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = min(dp[i][j+1], dp[i+1][j]) + grid[i][j]
        return dp[0][0]
s = Solution()
r = [[1,3,1],[1,6,1],[4,2,1]]
print(s.minPathSum(r))