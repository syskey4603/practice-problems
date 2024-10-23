def checkhaystack(haystack, needle, indexofhaystack):
    for y in range(len(needle)):
        if(haystack[indexofhaystack+y] != needle[y]):
            return -1

    return indexofhaystack



def strStr(haystack, needle):
    if(len(needle) > len(haystack)):
        return -1
    
    for x in range(len(haystack)-len(needle)+1):
        if(haystack[x] == needle[0]):
            if(checkhaystack(haystack, needle, x) == -1):
                continue
            else:
                return x
    return -1
            
            
                









haystack = "aghaaxagarw5r"
needle = "aaa"

print(strStr(haystack, needle))

'''

loop through the string until the first letter of the haystack is the same as the first letter of the needle
then loop through the needle and check if the letter is the same as the letter in the haystack until the last letter of needle
if not break out of the loop
if it is the same return start of needle


'''