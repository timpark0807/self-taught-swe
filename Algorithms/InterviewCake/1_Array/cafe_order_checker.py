def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    t_pointer = 0
    d_pointer = 0 
    
    for order in served_orders:
        if t_pointer < len(take_out_orders) and order == take_out_orders[t_pointer]:
            t_pointer += 1 
        elif d_pointer < len(dine_in_orders) and order == dine_in_orders[d_pointer]: 
            d_pointer += 1
        else:
            return False
    
    if t_pointer < len(take_out_orders) or d_pointer < len(dine_in_orders):
        return False
    return True



