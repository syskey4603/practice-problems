def maxProfit(prices):
    currentprice = prices[0]
    profit = 0
    for x in range(len(prices)):
        priceofx = prices[x]
        if(currentprice > priceofx):
            currentprice = priceofx
        elif(priceofx - currentprice > profit):
            profit = priceofx - currentprice
    return profit

        



prices = [7,2,5,3,6,1]
print(maxProfit(prices))



'''
loop through the prices and loop through all the other prices
subtract original value from the new loop value 
if its larger than previous profit then set it to previous profit

'''