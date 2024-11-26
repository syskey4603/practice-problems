def comparetriplet(a,b):
    returnarr = [0,0]
    for x in range(len(a)):
        if a[x] > b[x]:
            returnarr[0] +=1
        elif b[x] > a[x]:
            returnarr[1] +=1
    return returnarr

