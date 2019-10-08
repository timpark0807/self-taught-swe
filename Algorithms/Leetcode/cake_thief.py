def cake_thief(cake_tuples, capacity):
    bag = [0] * (capacity + 1)
    
    for bag_capacity in range(len(bag)):
        curr_max = 0
        for weight, value in cake_tuples:
            if weight <= bag_capacity:
                remaining = bag_capacity - weight
                curr_max = max(curr_max, value + bag[remaining])
        bag[bag_capacity] = curr_max
    return bag[-1]

ans = cake_thief([(1,3), (2,7), (3,8)], 3)
print(ans)
    
