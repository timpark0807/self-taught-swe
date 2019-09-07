def evenodd_2(arr):
    even, odd = 0, len(arr)-1
    
    while even < odd:
        if arr[even] % 2 == 0:
            even += 1
        else:
            arr[odd], arr[even] = arr[even], arr[odd]
            odd -= 1 
            
arr2 = [20, 4, 5, 15, 2, 6, 7]
print(evenodd2(arr2))

def evenodd(arr):
    boundary = 0
    
    while arr[boundary] % 2 == 0:
        boundary += 1
        
    for index in range(1, len(arr)):
        if arr[index] % 2 == 0:
            arr[index], arr[boundary] = arr[boundary], arr[index]
            boundary += 1

    return arr


arr = [20, 3 , 4, 5, 15, 2, 6, 7]
print(evenodd(arr))
