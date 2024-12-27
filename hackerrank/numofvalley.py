def numofvalley(path):
    curval = 0
    numofvalley = 0
    for x in path:
        if x == "U":
            curval +=1
        elif x == "D":
            curval -=1
       
        if curval == -1 and x == "D":
            numofvalley+=1
    return numofvalley