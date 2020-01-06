def rod_cutting(lengths, prices, n):
    return dp(lengths, prices, n, 0, 0)

def dp(lengths, prices, remain, index, profit):
    if index == len(lengths):
        return profit
    elif lengths[index] > remain:
        return dp(lengths, prices, remain, index+1, profit)
    else:
        cut = dp(lengths, prices, remain-lengths[index], index, profit + prices[index])
        skip = dp(lengths, prices, remain, index+1, profit)
        return max(cut, skip)

lengths = [1, 2, 3, 4, 5]
prices = [2, 6, 7, 10, 13]
n = 5
print(rod_cutting(lengths, prices, n))
