thisdict = {
  "(": ")",
  "{": "}",
  "[": "]"
}


def isValid(s):
    openbrack = []
    didbreak = False
    for x in range(len(s)):
        didbreak = False
        for item in thisdict.keys():
            if(s[x] == item):
                openbrack.append(s[x])
                didbreak = True
                break
        if(didbreak):
            continue
        
        if(openbrack == []):
            return False
        if(s[x] == thisdict[openbrack[len(openbrack)-1]]):
            openbrack.pop()
        else:
            return False
    if(openbrack==[]):
        return True
    else:
        return False
        



s = "]"

print(isValid(s))


''''
all incomplete brackets = []
start from the first char
For every charcter in the string, check if it is OPEN bracket
if it is OPEN bracket, ADD TO THE INCOMPLETE ARRAY
else if it is closed backet, check the last incomplete char 
    if it is matching, remove from incomplete and move to the next char in  the original array
    if it is not matching, then exit with false
    after all check if incomplete is empty if it is return false
    else return true


'''