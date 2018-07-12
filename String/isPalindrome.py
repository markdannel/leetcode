s = "0P"#"A man, a plan, a ccanal: Panama"

import re
s = re.sub('[^a-zA-Z0-9]','',s)
s = s.lower()

l = len(s)

i = 0
while i < (l+1)//2:
    if s[i] != s[l-1-i]:
        print("not equal")
    i += 1
print(l)