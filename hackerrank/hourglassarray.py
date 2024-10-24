'''

First repetition 

'''
'''
arr = [[0, -4 ,-6, 0, -7, -6], [-1, -2, -6, -8, -3, -1,], [-1, -1, -1, -2 ,-3 ,-4], [-3, -1 ,-2 ,-5 ,-7 ,-4], [-3 ,-5 ,-3 ,-6 ,-6, -6], [-3, -6, 0 ,-8 ,-6 ,-7]]

def hourglasssum(arr, startrow, startingval):
    addednum =0
    if(startrow > len(arr)-2):
        print("test")
        return 0
    if(startingval > 3):
        print("test")
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

highestnum = -999999999999999999999999

      
for z in range(len(arr)-2):
    for k in range(len(arr[z])-2):
        row = z
        startingval = k
        temp = hourglasssum(arr, row, startingval)
        if(temp == 0):
            print("test")
        if(temp > highestnum):
            highestnum = temp

print(highestnum)
'''
'''

Second repetition

'''



def anynumberofrowssum(arr, startrow, startcol):
    addnum = 0
    if startrow > len(arr)-2:
        return 0
    for x in range(startrow, len(arr)-1):
        if startcol > len(arr[x])-2:
            return 0
        for y in range(startcol, len(arr[x])):
            if x == startrow or x == startrow+2:
                if y > startcol+2:
                    break
                addnum += arr[x][y]
            elif x == startrow+1:
                addnum += arr[x][startcol+1]
                break
    return addnum






arrnew = [[1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 2, 4, 4],
    [0, 0, 0, 2, 0]
]
highestnumnew = -87472347274242424
for z in range(len(arrnew)-2):
    startrow = z
    for k in range(len(arrnew[z])-2):
        startcol = k

        temp = anynumberofrowssum(arrnew, startrow, startcol)
        if(temp > highestnumnew):
            highestnumnew = temp

print(highestnumnew)