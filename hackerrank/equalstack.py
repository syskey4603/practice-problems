def equalStack(h1,h2,h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    allheights = findheights(h1, h2, h3)
    lowestheight = allheights[0]
    while allheights[0] != allheights[1] or allheights[0] != allheights[2]:
        lowestheight = findlowestheight(allheights[0],allheights[1],allheights[2])

        if allheights[0] != lowestheight:
            allheights[0] -= h1.pop()
        if allheights[1] != lowestheight:
            allheights[1] -= h2.pop()
        if allheights[2] != lowestheight:
            allheights[2] -= h3.pop()

    return lowestheight
    
    

def findheights(h1, h2, h3):
    totalh1 = 0
    totalh2 = 0
    totalh3 = 0
    for x in h1:
        totalh1+=x
    for y in h2:
        totalh2 +=y
    for z in h3:
        totalh3 +=z
    return [totalh1, totalh2, totalh3]

def findlowestheight(totalh1,totalh2,totalh3):
    if totalh1 <= totalh2:
        if totalh1 <= totalh3:
            lowestval = totalh1
        else:
            lowestval = totalh3
    else:
        if totalh2 <= totalh3:
            lowestval = totalh2
        else:
            lowestval = totalh3
    return lowestval


h1 = [1, 1, 1, 1, 1]
h2 = [3, 2]
h3 = [1, 3, 1]
print(equalStack(h1,h2,h3))

'''

find the lowest height then remove the top element of the other stacks
repeat until all heights are the same
if two stacks have equal height remove from the other one

'''