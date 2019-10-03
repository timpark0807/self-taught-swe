
def max_duffel_bag_value(cake_tuples, weight_capacity):

    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        current_max_value = 0 
        for cake_weight, cake_value in cake_tuples:
            
            if cake_weight <= current_capacity:
                
                remaining_capacity = current_capacity - cake_weight 

                max_value_using_cake = cake_value + max_values_at_capacities[remaining_capacity]
                
                current_max_value = max(max_value_using_cake, current_max_value)
            
        max_values_at_capacities[current_capacity] = current_max_value
    print(max_values_at_capacities)
    return max_values_at_capacities[weight_capacity]


cake_tuples = [(1,1), (2,3), (3,3)]
print(max_duffel_bag_value(cake_tuples, 4))



#               max_value_using_cake should take the max_values_at_capacities of remaining_capacity 
#   Error:      max_value_using_cake = max_values_at_capacities[current_capacity] + cake_value
