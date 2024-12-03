def Panagram(s):
    allchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = s.lower()
    for x in s:
        if x in allchar:
            allchar.remove(x)
    
    if not allchar:
        print("panagram")
    else:
        print("not panagram")




s = "We promptly judged antique ivory buckles for the next prize"
print(Panagram(s))