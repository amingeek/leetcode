prices = [7,6,4,3,1]
#prices = [7,6,4,3,1] return 0
best_day = 0
def compute(prices):
    min_price = float('inf')  
    max_profit = 0  

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

print(compute(prices,))