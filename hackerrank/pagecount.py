def pageCount(n, p):
    if p == n or p == 1:
        return 0
    if p-1 < n-p:
        if (p-1)%2 == 0:
            return int((p-1)/2)
        elif (p-1)%2 != 0:
            return int(p/2)
    elif n-p <= p-1:
        if (n-1-p)%2 == 0:
            return int((n-1-p)/2)
        elif (n-1-p)%2 != 0:
            return int((n-p)/2)   


print(pageCount(6,5))