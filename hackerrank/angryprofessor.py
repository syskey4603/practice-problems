def angryProfessor(k, a):
    temp = 0
    for x in a:
        if x > 0:
            temp+=1
    if len(a)-temp<k:
        return "YES"
    return "NO"

    


k = 3
a = [-1, -3, 4, 2]
print(angryProfessor(k,a))