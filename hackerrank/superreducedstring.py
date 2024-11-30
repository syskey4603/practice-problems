'''

remove all the double letters 
removedletters=True
if its true repeat
if its false
stop and return whatever in the string



'''
def removeonce(s):
    startindex = 0
    finalindex = len(s)-1
    while startindex < finalindex:
        if s[startindex] == s[startindex+1]:
            s = s[:startindex] + s[startindex+2:]
            finalindex-=2
        else:
            startindex+=1
    return s
def superReducedString(s):
    stringremoved = True
    while stringremoved:
        removedstr = removeonce(s)
        if removedstr == s:
            stringremoved = False
        s = removedstr
    if s == "":
        s = "Empty String"
    return s



s = "abbacdef"
print(superReducedString(s))