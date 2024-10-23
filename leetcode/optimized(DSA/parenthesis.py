def validParenthesisfailed(s):
    bracketdict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    highvalue = len(s)-1
    lowvalue = 0

    for x in range(len(s)):
        try: 
            if(bracketdict[s[lowvalue]] != s[highvalue]):
                return False
            lowvalue+=1
            highvalue-=1
        except KeyError:
            return True

    return True




'''

create a dictionary for each with the open bracket being the key and the close the value
loop through the string with 2 pointers the high value and low value 
pass the lowvalue as the key and check if the lowvalue value is == the highvalue 
if its not return False
lowvalue +=1 
highvalue -=1 
at the end return true

'''


def validParenthesis(s):
    bracketdict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack =[]

    for x in s:
        if(x in bracketdict):
            stack.append(x)
        else:
            if(not stack):
                return False
            top = stack.pop()
            if(bracketdict[top] != x):
                return False
    if(stack):
        return False
    else:
        return True






s = "()[]{}"
print(validParenthesis(s))








'''
create dict with the open bracket as the key and close as the value 
since the most recent open bracket has to be closed before any other we can use a stack
add all the open brackets to a stack 
if the value is a closing bracket pop the top value and check if its the corresponding close 
if isnt return false
if it is a closing bracket and nothing is in stack return false
if there is something in stack after the loop return false
otherwise return true

'''