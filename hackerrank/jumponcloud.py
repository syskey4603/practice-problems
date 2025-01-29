def jumpingOnClouds(c):
    i = 0
    count = 0
    while i != len(c)-1:
        if i < len(c)-2 and c[i+2] == 0:
            i +=2
            count +=1
        else:
            i+=1
            count+=1
    return count
    



c = [0, 0, 1 ,0 ,0, 1 ,0]
print(jumpingOnClouds(c))