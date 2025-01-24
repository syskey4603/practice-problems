def libraryFine(d1, m1, y1, d2, m2, y2):

    if y1 > y2:
        return 10000
    elif y1 < y2:
        return 0 

    if m1>m2:
        return 500*(m1-m2)
    elif m1<m2:
        return 0 
    
    if d1>d2:
        return 15*(d1-d2)
    
    return 0

d1 = 6
m1 = 6
y1 = 2015
d2 = 9
m2 = 6
y2= 2016
print(libraryFine(d1, m1,y1,d2,m2,y2))