s = 'loveleetcode'

l = len(s)

arr = [50]*30

i = 0
while i < l:
    n = ord(s[i]) - 97
    if arr[n] == 50:
        arr[n] = i
    else:
        arr[n] = 100*i
    i += 1
res = min(*arr)

if res == 50:
    #return -1
    pass
print(arr, min(*arr))