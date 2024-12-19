def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 > v2:
        diffbetweenstart = x2-x1
        diffbetweenjump = v1-v2
        if factorfunc(diffbetweenjump, diffbetweenstart):
            return("YES")
        
    elif x1 > x2 and v1 < v2:
        diffbetweenstart = x1-x2
        diffbetweenjump = v2-v1
        if factorfunc(diffbetweenjump, diffbetweenstart):
            return("YES")



    return("NO")
    

def factorfunc(a, b):
    return(b%a==0)

x1 = 21
v1 = 6
x2 = 47
v2 = 3
print(kangaroo(x1,v1,x2,v2))


'''

if the first one starts earlier but has a larger jump its possible

if the diff between startings is greater 


'''