def getMoneySpent(keyboards, drives, b):
    final = -1
    for x in keyboards:
        for y in drives:
            if x+y > final and x+y<b:
                final = x+y
    return final

374623


keyboards = [3,1]
drives = [5,2,8]
b = 10
print(getMoneySpent(keyboards, drives, b))