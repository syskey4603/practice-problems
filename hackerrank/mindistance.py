def minimumDistances(a):
    returnval = 500
    for x in range(len(a)):
        for y in range(x+1, len(a)):
            if a[x] == a[y]:
                if y-x < returnval:
                    returnval = y-x
    
    if returnval == 500:
        return -1
    else:
        return returnval



a = [7,1,3,4,1,7]
print(minimumDistances(a))