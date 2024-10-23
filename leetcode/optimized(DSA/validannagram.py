def isAnnagram(s, t):
    if(len(s) != len(t)):
        return False
    
    count = {}

    for x in s:
        if(x in count):
            count[x]+=1
        else:
            count[x] = 1

    for y in t:
        if(y in count):
            count[y]-=1
        else:
            return False

    
    for value in count.values():
        if(value != 0):
            return False
    return True
        


s="bbcc"
t="ccbc"

print(isAnnagram(s, t))

'''
use dicts/hashmaps
loop through s and for every letter create a count
the letter is the key and the count is the value
now loop through t and do the same but subtract but if its not in it just return false

'''