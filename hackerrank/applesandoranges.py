def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleoutput = 0
    orangeoutput = 0
    for x in apples:
        if a + x >= s and a+x <= t:
            appleoutput +=1
    
    for y in oranges:
        if y+b >= s and y+b <= t:
            orangeoutput+=1
    
    print(appleoutput)
    print(orangeoutput)
    

s = 2
t = 3 
a = 1 
b = 5 
apples = [2]
oranges = [-2]

print(countApplesAndOranges(s,t,a,b,apples,oranges))