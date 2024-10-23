def addDigits(num):
    addnum = 0
    for x in str(num):
        addnum += int(x)
    return addnum

def main(num):
    while num > 9:
        num = addDigits(num)
    return num

def recursionmethod(num):
    if num < 10:
        return num
    else:
        added = 0
        for x in str(num):
            added += int(x)
        return recursionmethod(added)
    
print(recursionmethod(381119))


'''

while num is greater than 9 call add digits 


'''