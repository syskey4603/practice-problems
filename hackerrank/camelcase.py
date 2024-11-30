def camelCase(s):
    wordnum = 1
    for x in s:
        if x.isupper():
            wordnum+=1
    return wordnum



s = "theCatIsYellow"
print(camelCase(s))