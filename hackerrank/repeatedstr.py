def repeatedString(s, n):
    numofa = 0
    for i in s:
        if i == "a":
            numofa +=1
    returnval = numofa*(n//len(s))
    remainder = n%len(s)

    for x in range(remainder):
        if s[x] == "a":
            returnval +=1
 

    return returnval
    
    



    

s = "aba"
n = 10


print(repeatedString(s, n))


'''

find the closesat multiple of the length of the str to the new length 
multiply that with the number of a in s
then add that to the return val
then count from 0 to the diff between new length and closest multiple
if a is part of that count add one more
then return returnval

'''