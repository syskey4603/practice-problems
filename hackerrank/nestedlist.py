#not the problem solving this is part of the python problems a
nestedlist = []
for _ in range(int(input())):
    templist=[]
    name = input()
    score = float(input())
    templist.append(name)
    templist.append(score)
    nestedlist.append(templist)
lowest = 10000000
secondlowest = 10000000
for x in nestedlist:
    if x[1] < lowest:
        lowest = x[1]
for y in nestedlist:
    if y[1] == lowest:
        continue
    else:
        if y[1] < secondlowest:
            secondlowest = y[1]
returnlist = []
for z in nestedlist:
    if z[1] == secondlowest:
        returnlist.append(z[0])
returnlist.sort()
for i in returnlist:
    print(i)
        
