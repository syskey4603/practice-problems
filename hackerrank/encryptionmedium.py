import math
def encryption(s):
    colrowlist = []
    s = s.replace(" ", "")
    tempstr = ""
    row = math.floor(math.sqrt(len(s)))
    col = math.ceil(math.sqrt(len(s)))

    for x in range(0, len(s)):
        tempstr += s[x]
        if (x+1)%col==0:
            colrowlist.append(tempstr)
            tempstr = ""

    


        

    


s = "haveaniceday"
print(encryption(s))