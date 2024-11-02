def bigsum(arr):
    sum = 0
    for x in arr:
        sum+=x
    return sum


arr = [1000000001, 1000000002 ,1000000003 ,1000000004 ,1000000005]
print(bigsum(arr))