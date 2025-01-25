def cutTheSticks(arr):
    newarr = arr
    while newarr:
        print(len(newarr))
        newarr = removesmallest(newarr)
    


def removesmallest(arr):
    smallest = min(arr)
    newarr = []
    for x in range(len(arr)):
        arr[x] = arr[x]-smallest
        if arr[x]!=0:
            newarr.append(arr[x])
    return newarr


arr = [5, 4, 4, 2, 2, 8]
print(cutTheSticks(arr))