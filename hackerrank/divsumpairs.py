def divsumpair(n,k,ar):
    finalreturn = 0
    for x in range(n):
        for y in range(x+1, n):
            temp = ar[x] +ar[y]
            if temp%k==0:
                finalreturn+=1
    return finalreturn



n = 6
k = 3
arr = [1, 3, 2, 6, 1, 2]
print(divsumpair(n,k,arr))