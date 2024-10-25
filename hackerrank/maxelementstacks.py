
def getMax(operations):
    stacktest = []
    returnlist = []
    temp = 0
    for x in operations:
        splitx = x.split()
        if splitx[0] == '1':
            print(splitx[0])
            stacktest.append(splitx[1])
        elif splitx[0] == '2':
            stacktest.pop()
        elif splitx[0] == '3':
            temp = 0
            for y in stacktest:
                if int(y) > temp:
                    temp = int(y)
            returnlist.append(int(temp))
    return returnlist

operations = ["10", "1 97", "2", "1 20", "2", "1 26", "1 20", "2", "3", "1 91", "3"]


print(getMax(operations))