lastanswer = 0
def dynamicArray(n, queries):
  
    answers = []
    def query1(x, y, newarr):
        global lastanswer
        idx = (x^lastanswer)%n
        newarr[idx].append(y)
    def query2(x, y, newarr, answers):
        global lastanswer
        idx = (x^lastanswer)%n
        lastanswer = newarr[idx][y%len(newarr[idx])] 
        answers.append(lastanswer)
    newarr = []
    i=0
    while i != n:
        newarr.append([])
        i+=1
    for row in queries:
        whatorun = row[0]
        if whatorun == 1:
            query1(row[1], row[2], newarr)
        elif whatorun == 2:
            query2(row[1], row[2], newarr, answers)
    return answers






n = 2
queries = [[1, 0, 5],
[1, 1, 7],
[1 ,0 ,3],
[2, 1, 0],
[2, 1, 1]]

print(dynamicArray(n, queries))