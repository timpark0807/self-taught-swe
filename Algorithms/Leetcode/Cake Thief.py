def max_duffel_bag_value(cake_tuples, weight_capacity):
    bag = (weight_capacity + 1) * [0]
    bag[0] = 0
    
    for capacity in range(1, len(bag)):
        
        optimal_choice = 0 
        
        for weight, value in cake_tuples:
            
            if weight <= capacity:
                
                remaining = capacity - weight 
                optimal_choice = max(value + bag[remaining], optimal_choice)
   
        
        bag[capacity] = optimal_choice 



    return bag[-1]

