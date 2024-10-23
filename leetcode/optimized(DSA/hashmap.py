'''

Problem: Find the first non-repeating character in a string
Description: Given a string, find the first character that does not repeat. Return the character or -1 if all characters repeat.
Example:
Input: "leetcode"
Output: 'l'

'''

def firstNonRepeatingCharacter(str):
    letterInstances = {}
    for x in str:
        letterInstances.setdefault(x, 0)
        letterInstances[x] +=1
    
    for y in str:
        if(letterInstances[y] == 1):
            return y
    return -1





str = "racecar"
print(firstNonRepeatingCharacter(str))

'''
for each value in the string add one to the value and the letter is the key
at the end loop through the values and return the key of the first value that is 1
'''