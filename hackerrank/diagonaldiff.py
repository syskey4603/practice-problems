def diagonaldiff(arr):
    firstdiag = 0
    seconddiag = 0
    for x in range(len(arr)):
        firstdiag+=arr[x][x]
    for y in range(len(arr)-1, -1, -1):
        seconddiag+=arr[y][(len(arr[y])-1)-y]
    return abs(seconddiag-firstdiag)
    




arr = [[1 ,2 ,3], [4 ,5 ,6], [9,8,9]]
print(diagonaldiff(arr))