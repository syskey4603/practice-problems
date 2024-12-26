def sockMerchant(n, ar):
    truelast = False
    pairnum = 0
    ar.sort()
    for x in range(len(ar)-1):
        if truelast:
            truelast = False
            continue
        if ar[x] == ar[x+1]:
            pairnum+=1
            truelast = True
   
    return pairnum
       
