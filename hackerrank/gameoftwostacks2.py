
def allcombinations(maxsum, a,b):
    a.reverse()
    b.reverse()

    highestmoves, currentsum, alastmoveindex, blastmoveindex = twoStacks(maxsum, a,b)
    for currentlastmove in range(alastmoveindex, len(a)):
        currentsum -= a[currentlastmove]
        newhighestmoves = highestmoves - 1
        newhighestmoves, currentsum, blastmoveindex = findmaxmoves(currentsum, newhighestmoves, maxsum, b, blastmoveindex-1)
        if newhighestmoves > highestmoves:
            highestmoves = newhighestmoves

    return highestmoves, currentsum, alastmoveindex, blastmoveindex

def twoStacks(maxSum, a,b):
    blastmoveindex = len(b)-1
    highestmoves, currentsum, alastmoveindex =  findmaxmoves(0, 0, maxSum, a, len(a)-1)
    if currentsum < maxSum:
        highestmoves, currentsum, blastmoveindex = findmaxmoves(currentsum, highestmoves, maxSum, b, len(b)-1)
    return highestmoves, currentsum, alastmoveindex, blastmoveindex



def findmaxmoves(currentsum, currentmoves, maxsum, a, startindex):
    lastmoveindex = 0
    highestmoves = 0
    for x in range(startindex, -1, -1):

        if currentsum > maxsum:
            currentmoves -=1
            currentsum -= a[x+1]
            lastmoveindex = x+2
            highestmoves = currentmoves
            break
        
        currentsum += a[x]
        currentmoves += 1

    return highestmoves, currentsum, lastmoveindex




a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
maxsum = 10
print(allcombinations(maxsum, a,b))


'''

first loop through 1 list and find the num of values before it exceeds maxsum 
add that num to highestmoves
next try add as many values from the otherl ist until it exceeds maxsum
if its higher than highestmoves replace highestmoves with this
when it exceeds maxsum remove one of the values that u used from the original list and do it again until u have removed all values from the original list
return highestmoves

the problem is it goes to 6 in a lastmoveindex instead of the next one
next problem is for some reason its doing 2 times for the same b value
'''