class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # le = len(s)
        # if le == 1: return False
        # arr = []
        # for i in range(0, le):
        #     item = s[i]
        #     l = len(arr)
        #     if item == '{' or item == '[' or item == '(':
        #         arr.append(s[i])
        #     elif item == '}':
        #         if l > 0:
        #             if arr.pop() != '{': return False
        #         else: return False
        #     elif item == ']':
        #         if l > 0:
        #             if arr.pop() != '[': return False
        #         else: return False
        #     elif item == ')':
        #         if l > 0:
        #             if arr.pop() != '(': return False
        #         else: return False
        # if len(arr) > 0:
        #     return False
        # return True
        if len(s)%2 != 0:
            return False
        
        d = {'(' : ')', '[' : ']', '{' : '}'}
        l = []
        for i in s:
            if i in d:
                l.append(d[i])
            elif not l:
                return False
            elif i != l.pop():
                return False
        if l:
            return False
        else:
            return True

s = Solution()
ss= s.isValid('(){}[][[')
print(ss)
        