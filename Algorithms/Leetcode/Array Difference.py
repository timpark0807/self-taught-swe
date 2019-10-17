def ctci(array, k):
    
    count = 0
    freq = {}
    
    for num in array:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in array:
        if num + k in freq:
            count += 1    

    return count



array = [1,7,5,9,2,12,3]
ans = ctci(array, k=2)
print(ans)
