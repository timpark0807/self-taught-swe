def three_sum(arr, target):
    d = set()
    for num in arr:
        d.add(num)
    global_min = float('inf')
    
    for index in range(len(arr)-1):
        num1 = arr[index]
        new_target = target - num1
        
        for num2 in range(index+1, len(arr)):
            needed = new_target - num2
            if needed in d:
                return [num1, needed , num2]
            else:
                how_close = abs(target - num1 - num2)
                if how_close < global_min:
                    global_min = how_close
                    answer = [num1, needed, num2]
                    print(answer)
    return answer
    
    
print(three_sum([12, 3, 4, 1, 6, 9], 35))
