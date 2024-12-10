def twochar(s, newlist):
    checklist = newlist

    for x in checklist:
        count=0
        boolcheck = True
        for y in s:
            if boolcheck and y == x[0]:
                count+=1
                boolcheck = False
            elif not boolcheck and y == x[1]:
                count+=1
                boolcheck = True
            
            
        print(x + " count: " + str(len(s)-count))

#s = "abcabcab"
s = "asdcbsdcagfsdbgdfanfghbsfdab"
#s = "cabcabcab"
#s = "abcabcabc"
#s = "cabcabcabc"

def findallchar(s):
    returnlist = []
    for x in s:
        if x not in returnlist:
            returnlist.append(x)
    return returnlist

def findcomb(newlist):
    returnlist = []
    for x in range(len(newlist)-1):
        for y in range(x+1, len(newlist)):
            returnlist.append(newlist[x]+newlist[y])
    newlist.reverse()
    for x in range(len(newlist)-1):
        for y in range(x+1, len(newlist)):
            returnlist.append(newlist[x]+newlist[y])
    print(returnlist)
    return(returnlist)

twochar(s, findcomb(findallchar(s)))
