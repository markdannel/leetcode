# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

# 示例 1：

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

# 明确「状态」 -> 定义 dp 数组/函数的含义 -> 明确「选择」-> 明确 base case
class Solution:

    def climbStairs(self, n: int) -> int:
        memo = [0]*n
        def dpp(n):
            if n <= 2:
                return n
            if memo[n-1] > 0:
                return memo[n-1]
            memo[n-1] = dpp(n-1) + dpp(n-2)
            return memo[n-1]
        return dpp(n)
s=Solution()
print(s.climbStairs(5))
