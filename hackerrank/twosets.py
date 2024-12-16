def twosets(a, b):
    return len(checkmultiples(a, checkfactors(b)))
    

def checkfactors(b):
    allfac = []
    loopbool = False
    for x in range(1, b[0]+1):
        loopbool = False
        for y in b:
            if y%x != 0:
                break
            if y == b[len(b)-1]:
                loopbool = True
        if loopbool:
            allfac.append(x)
            
    return allfac


def checkmultiples(a, checklist):
    print(checklist)
    allfac = []
    loopbool = False
    for x in checklist:
        loopbool = False
        for y in a:
            if x%y != 0:
                break
            if y == a[len(a)-1]:
                loopbool = True
        if loopbool:
            allfac.append(x)
    return allfac
            


a = [2,4]
b = [16,32,96]
print(twosets(a,b))


'''

find the total nums in between both sets

the num has to be a multiple of all nums in a and a factor of the nums in b

first all the factors of the smaller num and check if its a factor of the other ones as well



'''