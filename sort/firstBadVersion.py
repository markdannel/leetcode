def firstBadVersion(n):

    arr = [False,False,False,False, True,True,True,True, True,True,True,]
    def isBadVersion(n):
        return arr[n]

    if isBadVersion(1): return 1
    mid = (n+1)//2
    fir = 1
    las = n
    while True:
        print("process:",mid)
        if isBadVersion(mid):
            las = mid
        else:
            fir = mid
        if las-fir == 1:
            return las
        mid = (las-fir)//2 + fir
        

n = firstBadVersion(6)
print(n)

