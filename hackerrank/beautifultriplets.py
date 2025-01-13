def beautifulTriplets(d, arr):
    temparr = []
    returnval = 0
    for x in range(len(arr)-2):
        temparr = []
        temparr.append(x)
        temparr.append(x+1)
        temparr.append(x+2)

        if verifytriplet(temparr, d, arr):
            returnval +=1
    
    return returnval



def verifytriplet(triplet, d, arr):
    i = triplet[0]
    j = triplet[1]
    k = triplet[2]

    if arr[j] - arr[i] == d and arr[k] - arr[j] == d:
        print(triplet)
        return True
    


arr = [2,2,3,4,5]
triplet = [0,2,3]
d = 1
#print(verifytriplet(triplet, d, arr))

print(beautifulTriplets(d,arr))