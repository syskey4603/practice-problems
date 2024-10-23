
arr = [[1,2,3,4,6], [4,5,6,7,8], [7, 8, 9,10,11], [10, 11, 12,5,6], [4, 8, 9,6,4]]

def hourglasssum(arr, startrow, startingval):
    addednum =0
    if(startrow > len(arr)-2):
        return 0
    if(startingval > 2):
        return 0
    for row in range(len(arr)):
        if(row == startrow or row == startrow+2):
            for col in range(startingval, len(arr[row])):
                if(col == startingval+3):
                    break
                addednum += arr[row][col]
        elif(row == startrow+1):
            addednum+=arr[row][startingval+1]
    return addednum



for z in range(len(arr)-2):
    row = z
    startingval = 0
    print(hourglasssum(arr, row, startingval))


