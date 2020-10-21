# 一条包含字母 A-Z 的消息通过以下方式进行了编码：

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。

# 示例 1:

# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:

# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

class Solution:
    def numDecodings(self, s: str) -> int:
        m = len(s)
        if m==0 or (m==1 and s=='0'):
            return 0
        if m==1:
            return 1
        dp = [0 for i in range(m)]
        dp[0],dp[1] = 1,2
        if s[0]=='0' or s[1]=='0' or int(s[0:2])>26: dp[1]=1
        for i in range(2,m):
            if s[i]!='0' and int(s[i-1:i+1])<=26:
                dp[i] = dp[i-1] + dp[i-2]
            elif int(s[i-1:i+1]) > 26:
                dp[i] = dp[i-1]
            elif int(s[i-1:i+1]) == 0:
                return 0
            else:
                dp[i] = dp[i-1]
                dp[i-1] = 0
        return dp[m-1]
s = Solution()
print(s.numDecodings('121021'))

