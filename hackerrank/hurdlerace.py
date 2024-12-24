def hurdleRace(k, height):
    maxnum = 0
    potionnum = 0
    for x in height:
        if x > maxnum:
            maxnum = x
    if maxnum > k:
        potionnum = maxnum-k
    else:
        return 0
    return potionnum
    




k = 1
height = [1,2,3,3,2]
print(hurdleRace(k, height))
