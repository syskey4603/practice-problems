def breakingRecords(scores):
    highcount = 0
    lowcount = 0
    highest = scores[0]
    lowest = scores[0]
    returnlist = []
    for x in scores:
        if x > highest:
            highcount+=1
            highest = x
        elif x < lowest:
            lowcount+=1
            lowest =x
    returnlist.append(highcount)
    returnlist.append(lowcount)
    return returnlist



scores = [10, 5 ,20 ,20 ,4 ,5, 2 ,25, 1]
print(breakingRecords(scores))