import string
import random

def randomsequence():
    randomchars = []
    intvalues = []
    for x in range(26):
        randomLetter = random.choice(string.ascii_lowercase)
        randomchars.append(randomLetter)
        intvalues.append(ord(randomLetter))
    return intvalues

    
def checksequence(sequence):
    sequencevalues = []
    lenofints = len(sequence)
    for x in range(lenofints-1):
        for y in range(x+1, lenofints):
            currentx = sequence[x]
            currenty = sequence[y]
            if currentx+1 != currenty:
                break
            else:
                sequencevalues.append(currentx)
                sequencevalues.append(currenty)
    return sequencevalues





def main():
    count = 0
    intvalues = randomsequence()
    sequencevalues = checksequence(intvalues)
    for x in range(len(sequencevalues)):
        count +=1
    return intvalues, count, sequencevalues




print(main())
'''
generate 26 random letters and store them in a list when storing store the number value in a seperate list
loop through the number list and loop for each element with all the others ahead
if y == x+1 then add 1 to count
return count


'''