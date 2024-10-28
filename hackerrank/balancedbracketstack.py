def checkBracket(s):
    returnstr = ""
    splitlines = s.splitlines()
    if splitlines[0].isnumeric():
        splitlines.pop(0)
    for line in splitlines:
        returnstr += checkline(line) + "\n"
    return returnstr.strip()



def checkline(line):
    bracketdict = {'{': '}', '[': ']', '(': ')'}
    openbracketstack = []
    if line[0] in bracketdict.values():
        return ("NO")

    for x in line:
        if x in bracketdict.keys():
            openbracketstack.append(x)
        elif x in bracketdict.values() and openbracketstack:
            topval = openbracketstack.pop()
            if bracketdict[topval] != x:
                return ("NO")
    if openbracketstack:
        return "NO"
    return ("YES")


s = """{{}("""




print(checkBracket(s))