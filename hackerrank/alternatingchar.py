def alternatingCharacters(s):
    count = 0
    for x in range(len(s)-1):
        if s[x] != s[x+1]:
            continue
        else:
            count+=1
    return count

def removeonce(s):
    news = s
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            news = news[:x] + news[x + 1:]
    return news

s = "AAAA"
print(alternatingCharacters(s))