class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxp = 0
        strMap = {}
        count = 0
        for str in s:
            if str not in strMap:
                count += 1
                strMap[str] = count
            else:
                nm = strMap[str]
                maxp = max(maxp, count)
                count = count - nm + 1
                for k in list(strMap):
                    if strMap[k] < nm:
                        strMap.pop(k)
                    else:
                        strMap[k] -= nm 

                strMap[str] = count
        return maxp
            


str = 'abcabcbb'#'pwwkew'#'abcdabcebb'
s=Solution()
n=s.lengthOfLongestSubstring(str)
print(n)