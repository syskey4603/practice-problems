def birthday(s, d, m):
    returnval = 0
    for x in range(len(s)-m+1):
        tempsum = 0
        for y in range(x, x+m):
            tempsum+=s[y]
        if tempsum == d:
            print(tempsum, s[x])
            returnval+=1
        return returnval





s = [1, 2, 1, 3, 2]
d = 3
m = 2

print(birthday(s,d,m))