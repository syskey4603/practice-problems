def isPallindrome(x):
    strx = str(x)
    oppstr = ""
    for y in range(len(strx)-1, -1, -1):
        oppstr = oppstr + str(strx[y])
    if(strx == oppstr):
        return True
    else:
        return False
    
print(isPallindrome(121))