def migratorybirds(arr):
    highestfreq = 1
    arr.sort()
    valdict = {}
    temp = 0
    for x in range(len(arr)):
        tempfreq = 1
        for y in range(x+1, len(arr)):
            if arr[x] == arr[y]:
                tempfreq+=1
            else:
                break
            if tempfreq > highestfreq:
                highestfreq=tempfreq
                valdict[arr[x]] = tempfreq

    for key in valdict.keys():
        if valdict[key] > temp:
            temp = key
    return temp
        
            
        


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4,4,4,4,4,4,4]
print(migratorybirds(arr))