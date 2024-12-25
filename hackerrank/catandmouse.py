def catAndMouse(x, y, z):
    adistance = abs(z-x)
    bdistance = abs(z-y)

    if adistance<bdistance:
        return("Cat A")
    elif bdistance<adistance:
        return("Cat B")
    elif adistance==bdistance:
        return("Mouse C")




x = 2
y = 5
z = 4
print(catAndMouse(x,y,z))