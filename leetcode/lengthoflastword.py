def lengthOfLastWord(s):
    count = 0
    for x in range(len(s)-1, -1, -1):
        if(count >= 1):
            if(s[x] == ' '):
                return count
        if(s[x] != ' '):
            count+=1
    return count




s = "b a "
print(lengthOfLastWord(s))



'''


loop through the string in reverse and begin count when we get a non space char
count until we find a space and return the count


'''