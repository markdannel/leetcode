# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        dp = [[False for j in range(size)] for i in range(size)]
        for i in range(size):
            dp[i][i] = True
        maxx, maxE = 1, 0
        for i in range(size-2,-1,-1):
            for j in range(i+1, size):
                curL = j-i+1
                if s[i] == s[j] and (curL <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if curL > maxx:
                        maxx = curL
                        maxE = i
                else:
                    dp[i][j] = False
                
        return s[maxE:maxE+maxx]

s = Solution()
print(s.longestPalindrome("acab"))