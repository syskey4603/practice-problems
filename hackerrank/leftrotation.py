def leftRotation(d, arr):            
    for x in range(d):
        indexzero = arr.pop(0)
        arr.append(indexzero)
    return arr





d = 1
arr = [1,2,3,4,5]
print(leftRotation(d, arr))