def anagram(s):
    if len(s)%2 != 0:
        return -1
    firststr = ""
    secondstr = ""
    tempset = []
    for x in range(int(len(s)/2)):
        firststr+=s[x]
    for y in range(int(len(s)/2), len(s)):
        secondstr+=s[y]
    
    if firststr == secondstr:
        return 0
    for z in firststr:
        tempset.append(z)
    
    for a in secondstr:
        if a in tempset:
            tempset.remove(a)
    
    return len(tempset)
    





s = "abaa"
print(anagram(s))