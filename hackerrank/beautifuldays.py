
def beautifulDays(i, j, k):
    returnval = 0
    for x in range(i,j+1):
        reverse = ""
        minus = 0
        reverse = int(str(x)[::-1])
        minus = abs(x-reverse)
        if minus%k == 0:
            returnval+=1
    return returnval


        


i = 20
j = 23
k = 6
print(beautifulDays(i,j,k))