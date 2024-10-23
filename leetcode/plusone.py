def plusOne(digits):
    newlist = []
    new_string = ''
    for i in digits:
        new_string += str(i)
    new_string = int(new_string) + 1
    new_string = str(new_string)


    for x in new_string:
        newlist.append(int(x))
    return newlist


digits = [1,2,3]
print(plusOne(digits))


'''
loop through the list add each item to a string
convert the string into an int and add one to it
loop through the new string and add each item to a list and return that list


'''