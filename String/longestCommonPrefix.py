strs = ['flower', 'flow', 'flight', 'af']

i = 0
k = 1
lstrs = len(strs)

# if lstrs == 0: return ""
# if lstrs == 1: return strs[0]
res = strs[0]
while k < lstrs:
    i = 0
    s1 = res
    s2 = strs[k]
    l1 = min(len(s2), len(s1))
    res = ''
    while i < l1:
        if s1[i] == s2[i]:
            res += s1[i]
            i += 1
        else:
            break
    k += 1
print(res)