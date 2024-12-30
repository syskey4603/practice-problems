import math

def viralAdvertising(days):
    shared = 5
    likes = 0
    returnlikes = 0
    for day in range(1, days+1):
        likes = math.floor(shared/2)
        returnlikes = returnlikes+likes
        shared = likes*3
    return returnlikes






days = 5
print(viralAdvertising(days))