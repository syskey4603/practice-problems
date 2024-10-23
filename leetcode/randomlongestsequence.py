import random

def randomsequence():
    randomnums = []
    for x in range(1,14):
        randomnums.append(random.randint(1,13))
    randomnums.sort()
    return randomnums

def findsequence(index, indexend, sequence):
    sequencearray = [sequence[index]]

    
    for x in range(index, indexend):
        if(len(sequencearray) == 13):
            return sequencearray
        if(x == len(sequence)-1):
            if(sequence[x] == 13 and sequence[0] == 1):
                if(len(sequencearray) == 12):
                    sequencearray.append(1)
                    return sequencearray
                sequencearray += (findsequence(0, index-1, sequence))
                return sequencearray
        elif sequence[x]+1 == sequence[x+1]:
            sequencearray.append(sequence[x+1])
        elif(sequence[x] != sequence[x+1]):
            break

    return sequencearray


def main(randomnums):
    print(randomnums)
    sequencenum = 0
    #return findsequence(2, len(randomnums), randomnums)
    
    for x in range(len(randomnums)):
        currentsequence = findsequence(x, len(randomnums), randomnums)
        if(len(currentsequence) > sequencenum):
            sequencenum = len(currentsequence)
            largestsequence = currentsequence
    return sequencenum, largestsequence
    


randonums = randomsequence()
print(main(randonums))
'''
generate 12 random numbers from 1 to 13 including 1 and 13
find the longest sequence possible for example 2,3 is shorter than 5,6,7

next level treat 13 and 1 as sequence for example 12,13,1 is a sequence



logic 



'''