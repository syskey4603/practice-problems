def mostMoves(maxSum, a, b):
    a.reverse()
    b.reverse()
    currentsum = 0
    movesreturn = 0
        
    while currentsum <= maxSum:
        if not a and not b:
            currentsum = maxSum+5
            movesreturn+=1
            continue
        if not a and b:
            currentsum +=b[-1]
            b.pop()
            movesreturn+=1
            continue
        if not b and a:
            currentsum += a[-1]
            a.pop()
            movesreturn +=1
            continue


        if a[-1] <= b[-1]:
            currentsum += a[-1]
            a.pop()
            movesreturn +=1
            continue
        else:
            currentsum +=b[-1]
            b.pop()
            movesreturn+=1


    movesreturn-=1
    return movesreturn






if __name__ == '__main__':
    inputstr = ['17 26 62',
    '7 15 12 0 5 18 17 2 10 15 4 2 9 15 13 12 16',
    '12 16 6 8 16 15 18 3 11 0 17 7 6 11 14 13 15 6 18 6 16 12 16 11 16 11',
    '31 34 5',
    '4 11 16 0 18 17 9 13 7 12 16 19 2 15 5 13 1 10 0 8 0 6 16 12 15 7 1 6 19 16 2',
    '15 8 11 16 6 0 5 11 7 9 8 6 3 3 4 8 17 14 9 5 15 15 1 19 10 0 12 8 11 9 11 18 17 14',
    '25 14 55',
    '11 6 1 13 14 7 8 10 3 17 7 18 6 4 5 13 17 4 16 9 17 16 12 6 7',
    '10 15 13 17 10 7 0 16 8 13 11 8 14 13',
    '44 42 13',
    '13 9 16 18 2 5 15 10 14 4 7 18 2 6 8 17 0 5 7 7 6 3 8 11 6 8 5 19 11 8 3 5 17 19 15 12 16 10 2 2 6 9 0 8',
    '16 9 17 16 6 4 15 12 0 3 16 6 11 1 18 15 10 13 12 19 5 7 11 1 10 14 4 16 3 4 17 11 5 14 19 12 19 15 4 11 10 12',
    '20 35 67',
    '19 9 8 13 1 7 18 0 19 19 10 5 15 19 0 0 16 12 5 10',
    '11 17 1 18 14 12 9 18 14 3 4 13 4 12 6 5 12 16 5 11 16 8 16 3 7 8 3 3 0 1 13 4 10 7 14',
    '37 50 64',
    '15 5 18 19 19 2 4 17 7 16 14 5 19 2 5 7 5 12 15 1 7 8 2 12 12 4 19 18 1 11 2 16 16 0 7 7 15',
    '3 5 14 19 19 19 18 1 16 17 6 0 13 19 7 1 1 12 5 6 11 3 19 14 5 7 3 18 14 10 13 10 15 19 9 14 11 0 7 7 17 6 8 10 5 7 3 7 19 8',
    '6 44 73',
    '16 17 9 3 12 19',
    '9 3 4 19 18 4 1 5 15 1 12 2 18 18 2 1 4 10 4 3 1 13 0 4 17 16 14 6 11 6 6 0 9 10 12 0 14 13 5 1 14 9 4 4',
    '21 19 58',
    '16 8 2 11 2 7 11 6 4 19 12 2 2 11 0 14 12 3 6 12 9',
    '19 9 11 5 11 7 2 11 5 19 7 14 13 18 8 12 1 14 8',
    '13 10 92',
    '14 10 11 8 14 14 15 7 16 6 8 7 4',
    '19 14 6 2 19 17 9 5 11 19',
    '4 24 81',
    '0 12 12 19',
    '15 6 1 18 7 15 5 14 14 1 12 15 8 16 14 2 14 9 13 12 18 19 3 18',
    '13 49 91',
    '4 2 3 3 17 1 16 8 0 12 13 14 18',
    '14 7 13 14 15 0 8 10 9 1 2 19 12 17 17 17 15 0 1 10 3 17 7 16 13 7 17 17 0 3 16 14 10 1 0 6 13 8 16 2 10 10 14 2 7 3 19 2 3',
    '12 23 87',
    '10 12 15 3 19 12 13 12 15 1 18 18',
    '2 19 16 16 7 12 10 9 2 16 12 1 0 3 3 3 16 8 2 6 12 17 2',
    '34 22 16',
    '7 8 16 6 6 18 17 14 6 4 18 9 14 0 5 18 13 5 13 9 1 10 9 3 8 1 12 10 16 5 17 16 5 13',
    '2 12 4 19 18 2 15 17 3 1 9 9 19 3 6 13 12 19 15 1 14 15',
    '5 19 67',
    '10 3 15 18 9',
    '9 0 13 5 11 11 7 7 8 11 8 18 12 0 13 18 5 5 10',
    '43 7 65',
    '7 0 3 5 2 6 1 1 7 10 13 0 15 5 4 14 4 4 5 4 14 17 16 7 8 1 12 18 13 10 14 1 10 17 6 5 16 19 18 3 1 11 16',
    '8 8 12 3 4 16 0',
    '20 12 11',
    '5 18 18 19 3 8 12 13 14 5 16 12 4 1 0 3 19 15 17 2',
    '11 5 11 3 8 7 12 1 8 3 11 14',
    '24 2 46',
    '16 1 17 2 15 15 18 19 11 19 19 14 10 15 3 12 18 9 15 14 9 3 6 10',
    '11 1',
    '12 28 75',
    '2 2 3 3 12 5 11 19 15 10 10 14',
    '10 16 16 17 0 0 15 9 16 1 18 11 19 9 14 0 2 4 7 17 6 2 12 10 7 3 1 2']


    for g_itr in range(4, 18):

        maxSum = int(inputstr[g_itr*3].split()[2])


        a = list(map(int, inputstr[g_itr*3+1].split()))


        b = list(map(int, inputstr[g_itr*3+2].split()))


        result = mostMoves(maxSum, a, b)

        print(str(result) + '\n')







'''
5
4 11 16 0 18 17 9 13 7 12 16 19 2 15 5 13 1 10 0 8 0 6 16 12 15 7 1 6 19 16 2
15 8 11 16 6 0 5 11 7 9 8 6 3 3 4 8 17 14 9 5 15 15 1 19 10 0 12 8 11 9 11 18 17 14

'''