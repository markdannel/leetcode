class Solution:
    def pushDominoes(self, dominoes):
        arr = []
        for i in dominoes:
            arr.append(i)
            
        l = len(arr)
        end = True
        
        while end:
            end = True
            flag= [False]*l

            for i in range(0, l):
                if arr[i] == 'L':
                    if i > 0 and arr[i-1] == '.':
                        if i > 1 and arr[i-2] != 'R':
                            arr[i-1] = 'L'
                            flag[i-2] = True
                            end = False
                        elif i == 1 and arr[0] == '.':
                            arr[0] = 'L'
                            end = False

            for i in range(0, l):
                if arr[i] == 'R':
                    if i < l-1 and arr[i+1] == '.':
                        if i < l-2 and arr[i+2] != 'L':
                            arr[i+1] = 'R'
                            end = False
                        elif flag[i+1] and arr[i+2]!='L':
                            arr[i+1] = 'R'
                            end = False
                        elif i == l-2 and arr[l-1] == '.':
                            arr[l-1] = 'R'
                            end = False
        s = ''
        for i in arr:
            s += str(i)
        return s

st = '.L.R...LR..R..'#'.L.R...LR..L..'
s = Solution()
ss = s.pushDominoes(st)
print(ss)