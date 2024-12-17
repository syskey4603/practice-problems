def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 > v2:
        if abs(v1-v2) > abs(x1-x2):
            print("NO")
        
    elif x1 > x2 and v1 < v2:
        if abs(v1-v2) > abs(x1-x2):
            print("NO")
    else:
        print("NO")
    



x1 = 21
v1 = 6
x2 = 47
v2 = 3
print(kangaroo(x1,v1,x2,v2))


'''

if the first one starts earlier but has a larger jump its possible

if the diff between startings is greater 


'''