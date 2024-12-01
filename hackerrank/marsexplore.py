def marsexplore(s):
    finalnum = 0
    count = 1
    for x in s:

        if count == 1:
            if x != "S":
                finalnum+=1
        elif count == 2:
            if x != "O":
                finalnum+=1
        elif count == 3:
            if x != "S":
                finalnum+=1
            count = 1
            continue
        count += 1

    return finalnum

        





s = "OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"
print(marsexplore(s))