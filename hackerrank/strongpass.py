def strongPass(s):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    numtrue = False
    lowertrue = False
    uppertrue = False
    specialtrue = False
    numtoadd = 0

    for x in s:
        if x in numbers:
            numtrue = True
        elif x in lower_case:
            lowertrue = True
        elif x in upper_case:
            uppertrue = True
        elif x in special_characters:
            specialtrue = True
    
    if not numtrue:
        numtoadd += 1
    if not lowertrue:
        numtoadd += 1
    if not uppertrue:
        numtoadd += 1
    if not specialtrue:
        numtoadd += 1

    if len(s) + numtoadd < 6:
        temp = len(s) + numtoadd
        temp = 6-temp
        numtoadd = numtoadd + temp
    
    return numtoadd

        


s = "2b"
print(strongPass(s))