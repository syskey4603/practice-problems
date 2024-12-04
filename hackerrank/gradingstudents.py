def gradeone(grades):
    if grades < 38 or grades%5 == 0:
        return grades
    finalgrade = ""
    strgrade = str(grades)
    unitval = int(strgrade[1])
    tenval = int(strgrade[0])

    if unitval > 2 and unitval < 5:
        unitval = 5
    elif unitval > 7:
        unitval = 0
        tenval+=1
    
    finalgrade = str(tenval) + str(unitval)
    finalgrade = int(finalgrade)

    return finalgrade
    
    
def gradingstudents(grades):
    for x in grades:
        return gradeone(x)



grades = [43, 32, 38, 79]
print(gradingstudents(grades))