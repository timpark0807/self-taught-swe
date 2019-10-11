def house_robber(houses):
    bag = [0] * len(houses)
    bag[0] = houses[0]
    bag[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        bag[i] = max(houses[i] + bag[i-2], bag[i-1])

    return bag[-1]






houses = [2, 1, 1, 1, 2]
ans = house_robber(houses)
print(ans)
