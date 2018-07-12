class Solution:
    def romanToInt(self, s):
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,
        'D':500, 'M':1000}
        arr = []
        sum = 0
        temp= 0
        for i in s:
            arr.append(dic[i])
        l = len(arr)
        for i in range(0, l-1):
            if arr[i+1]>arr[i]:
                sum -= arr[i]
            else:
                sum += arr[i]
        sum += arr[l-1]
        
        print(arr, sum)

s = Solution()
ss = "MCMXCIV"#1994#"LVIII"#58
s.romanToInt(ss)
