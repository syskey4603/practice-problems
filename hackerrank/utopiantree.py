def utopianTree(n):
    numreturn = 1
    for x in range(1,n+1):
        if x%2==0:
            numreturn+=1
        else:
            numreturn=numreturn*2
    return numreturn



n = 5
print(utopianTree(n))