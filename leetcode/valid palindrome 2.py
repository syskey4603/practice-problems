def validpalindrome(s):
    reversestr = s[::-1]
    if(s == reversestr):
        return True

    for x in range(len(s)):
        tempstr = s[:x] + s[x + 1:]
        if(tempstr[::-1] == tempstr):
            return True

    return False

s = "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"
print(validpalindrome(s))


'''
first check if itd already is a pallindrome if it is return true
if not loop through the word and for every letter renmove it and check if it is a pallindrome if it is return true if not at the end return false


'''