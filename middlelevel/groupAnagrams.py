class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        l = len(strs)
        if l == 0:
            return []
        if l == 1:
            return [strs]
        res = []
        strMap = {}
        for str in strs:
            thiss = ''.join(sorted(str))
            if thiss not in strMap:
                strMap[thiss] = len(res)
                res.append([str])
            else:
                res[strMap[thiss]].append(str)
        return res


arr = ["ray","cod","abe","ned","arc","jar","owl","pop"
      ,"paw","sky","yup","fed","jul","woo","ado","why"
      ,"ben","mys","den","dem","fat","you","eon","sui"
      ,"oct","asp","ago","lea","sow","hus","fee","yup"
      ,"eve","red","flo","ids","tic","pup","hag","ito"
      ,"zoo"]#["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
res = s.groupAnagrams(arr)
print(res)