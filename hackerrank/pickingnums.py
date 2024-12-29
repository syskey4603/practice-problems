def eachelement(a, el):
    a.sort()
    newarr = []
    for x in range(el, len(a)):
        if not newarr or newarr[0] == a[x] or abs(newarr[0]-a[x]) == 1:
            newarr.append(a[x])
    return newarr

def pickingnums(a):
    returnlist = []
    curvals = []
    largelen = 0
    for x in range(len(a)):
        curvals = eachelement(a, x)
        if len(curvals) > largelen:
            largelen = len(curvals)
            returnlist = curvals
    return len(returnlist)




a = [
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
    66, 66, 66, 66, 66, 66, 66, 66, 66, 66
]

print(pickingnums(a))