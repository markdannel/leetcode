s = "anagram"
t = "nagaram"

ls = len(s)
lt = len(t)
if ls != lt:
    print("not equel")
s = sorted(s)
t = sorted(t)

i  = 0
while i < ls:
    if s[i] != t[i]:
        print("not2")
    i += 1
print("not3")
