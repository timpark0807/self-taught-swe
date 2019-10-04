def min_coins(coins, amount):
    
    table = [0] * (amount + 1)

    for current_amount in range(1, amount + 1):
        
        current_min = amount+1
        
        for coin in coins:
            
            if coin <= current_amount:

                remaining = current_amount - coin

                current_min = min(table[remaining] + 1, current_min)

        table[current_amount] = current_min
    
    return table[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    ans = min_coins(coins, amount)
    print(ans)

