def bonAppetit(bill, k, b):
    realbill = 0
    for x in range(len(bill)):
        if x ==k:
            continue
        realbill += bill[x]
    if realbill/2 == b:
        print("Bon Appetit")
    else:
        print(int(b-realbill/2))



bill = [3, 10, 2, 9]
k = 1
b = 12
print(bonAppetit(bill, k, b))
