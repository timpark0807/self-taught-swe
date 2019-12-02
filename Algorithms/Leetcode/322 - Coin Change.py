def coin_change(coins, amount):
    """

    change = 1

    coin = [1, 2, 5]




    [0, 0, 0, 0, 0, 0, 0]
     0  1  2  3  4  5  6 

    """
    table = [float('inf')] * (amount + 1)
    table[0] = 0
    
    for change in range(1, len(table)):
        for coin in coins:
            if coin <= change:
                table[change] = min(table[change], table[change-coin] + 1)

    return table[-1]




coins = [1, 2, 5]
amount = 11

print(coin_change(coins, amount))
