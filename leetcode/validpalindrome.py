def checkPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


def Main(s):

    sedited = ""
    for x in range(len(s)):
        if(s[x].isalnum()):
            sedited += s[x]
    sedited = sedited.lower()
    
    if checkPalindrome(sedited):
        return True 
    else:
        return False

s = "A man, a plan, a canal: Panama"


Main(s)