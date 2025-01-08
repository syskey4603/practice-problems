def equalizeArray(arr):
    hashset = {}
    maxval = 0
    for x in arr:
        if x not in hashset:
            hashset[x] = 1
        else:
            hashset[x] +=1
        if hashset[x] > maxval:
            maxval = hashset[x]
    return len(arr)-maxval

    



arr = [3,3,2,1,3]

print(equalizeArray(arr))