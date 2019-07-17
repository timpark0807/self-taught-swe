def add_up_rec(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + add_up_rec(arr[1:])
        
print(add_up_rec([2,4,6]))
    
