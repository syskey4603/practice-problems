def anagram(query, dict):
    if len(query) != len(dict):
        return False
    tempset = []
    for x in dict:
        tempset.append(x)

    for y in query:
        if y in tempset:
            tempset.remove(y)
    if not tempset:
        return True
    else:
        return False



query = "aabbcc"
dict = "aabbc"
print(anagram(query,dict))