prices = [7,1,5,3,6,4]
#prices = [7,1,5,3,6,4] return 7
def compute(prices):  
    sum_profit = 0
    for i in range(0,len(prices)-1):
        if (prices[i+1] - prices[i]) > 0:
            sum_profit += (prices[i+1] - prices[i])
    
    return sum_profit

print(compute(prices,))