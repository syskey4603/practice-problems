def staircase(n):
    for x in range(1,n+1):
        for _ in range(n-x):
            print(" ", end='')
        for y in range(x):
            print("#", end='')
        print("")

staircase(6)