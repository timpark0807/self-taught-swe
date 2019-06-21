def count_list(arr):
    if arr = []:
        return 0
    else:
        return count_list(arr[1:])



print(count_list([5,3,2,7]))
