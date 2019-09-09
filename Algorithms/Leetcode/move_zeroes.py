def move_zeroes(arr):

    boundary, current = 0, 0

    while current < len(arr):
        if arr[current] != 0:
            arr[current], arr[boundary] = arr[boundary], arr[current]
            boundary += 1
            
        current += 1

    return arr


#     b
#        c
arr= [0, 12, 0, 1, 2, 0]
print(move_zeroes(arr))
