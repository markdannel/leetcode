s = "hello"

l = len(s)

i = 0
t = []
sn = ""
while i < l:
    t.append(s[i])
    i += 1

i = 0

while i < l:
    sn += t.pop()
    i += 1

print(sn)

