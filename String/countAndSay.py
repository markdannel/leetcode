n = 50

i = 2
s = '11'
if n == 1:
    print('11')
    # return '11'
while i < n:
    l = len(s)
    j = 1
    count = 1
    nexts = ''
    while j < l:
        if s[j] == s[j-1]:
            count += 1
        else:
            nexts += str(count) + s[j-1]
            count = 1
        j += 1
    nexts += str(count) + s[j-1]
    i += 1
    s = nexts
print(s)

