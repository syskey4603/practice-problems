def pickingnums(a):
    a.sort()
    newarr = []
    for x in range(len(a)-1):
        if a[x] == a[x+1] or a[x]+1==a[x+1]:
            newarr.append(a[x])
    return newarr

a = [4, 6, 5, 3, 3, 1]
print(pickingnums(a))