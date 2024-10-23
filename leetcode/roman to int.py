allnums = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}
def romantoint(roman):
    total = 0
    skipnext = False
    for x in range(len(roman)-1):
        if(skipnext == True):
            skipnext = False
            continue
        if(allnums[roman[x]] < allnums[roman[x+1]]):
            total += allnums[roman[x+1]] - allnums[roman[x]]
            skipnext = True
        elif(allnums[roman[x]] > allnums[roman[x+1]]):
            total += allnums[roman[x]]
            skipnext = False

        elif(allnums[roman[x]] == allnums[roman[x+1]]):
            total += allnums[roman[x]]
            skipnext = False

    if(allnums[roman[len(roman)-1]] == allnums[roman[len(roman)-2]] or allnums[roman[len(roman)-1]] < allnums[roman[len(roman)-2]]):
        total += allnums[roman[len(roman)-1]]

    return total
    


print(romantoint("MDCXCV"))




'''
first create dictionary for all the roman numbers and the corelating value
loop through the roman numbers and check if the one after the first letter is smaller larget or equal


'''