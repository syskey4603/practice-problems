def makinganagram(s1, s2):
    str1set = []
    str2set = []
    finalreturn = 0
    for x in s1:
        str1set.append(x)
    
    for y in s2:
        str2set.append(y)
    
    
    return finalreturn
        




s1 = "absdjkvuahdakejfnfauhdsaavasdlkj"
s2 = "djfladfhiawasdkjvalskufhafablsdkashlahdfa"
print(makinganagram(s1, s2))
