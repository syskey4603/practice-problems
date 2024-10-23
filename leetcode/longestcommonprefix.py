def lcp(strs):
    prefix = ""
    for x in range(len(strs[0])):
        lettercompare = strs[0][x]
        for y in range(1, len(strs)):
            if(x > len(strs[y])-1):
                return prefix
            if(lettercompare != strs[y][x]):
                return prefix
        prefix += lettercompare
    return prefix

strs = ["flower","flow","flows"]
print(lcp(strs))






'''
Input: strs = ["flower","flow","flight"]
Output: "fl"

loop through the first word get the letter through the loop and check for the corelating letter for all other words if its equal add it to the prefix if its not return the prefix

'''