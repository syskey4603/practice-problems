def arrayManipulation(n, queries):
    returnlist = []
    for lislen in range(n):
        returnlist.append(0)
    
    for x in queries:
        for z in range(x[0]-1, x[1]):
            returnlist[z] += x[2]

    temp = 0

    for val in returnlist:
        if val > temp:
            temp = val
    return temp




n = 5
queries = [[1,2,100], [2,5,100], [3,4,100]]
print(arrayManipulation(n, queries))