# haystack = 'helooloi llo'
# needle = 'll'
haystack = "mississippi"
needle = "issip"

l1 = len(haystack)
l2 = len(needle)

i = j =0
prei = 0
res = 0
while i < l1 and j < l2:
    if haystack[i] == needle[j]:
        j += 1
        prei += 1
    else:
        j = 0
        i -= prei
        prei = 0
    i += 1
if j == l2:
    print("position = ", i-j, j, i)
