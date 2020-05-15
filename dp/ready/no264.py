# 编写一个程序，找出第 n 个丑数。

# 丑数就是质因数只包含 2, 3, 5 的正整数。

# 示例:

# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  

# 1 是丑数。
# n 不超过1690。
import math
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1]
        i2,i3,i5=0,0,0
        for i in range(1,n):
            dp.append(min(dp[i2]*2,dp[i3]*3,dp[i5]*5))
            if dp[i2]*2==dp[i]: i2+=1
            if dp[i3]*3==dp[i]: i3+=1
            if dp[i5]*5==dp[i]: i5+=1
        return dp[-1]
s=Solution()
print(s.nthUglyNumber(20))