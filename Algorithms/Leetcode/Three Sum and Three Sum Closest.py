def three_sum(arr, target):
    """
      i
      0  1  2  3  4  5
     [1, 3, 4, 6, 9, 12]
         l           r

        
    """
    arr.sort()

    for i in range(len(arr)):
        left = i + 1
        right = len(arr)-1
        needed = target - arr[i]
        while left < right:
            if arr[left] + arr[right] == needed:
                return [arr[i], arr[left], arr[right]]
            elif arr[left] + arr[right] > target:
                right -= 1
            else:
                left += 1
    return False

def three_sum_closest(arr, target):
    """
      i
      0  1  2  3  4  5
     [1, 3, 4, 6, 9, 12]
         l           r

        
    """
    arr.sort()
    global_closest = float('inf')
    
    for i in range(len(arr)):
        left = i + 1
        right = len(arr)-1
        needed = target - arr[i]
        while left < right:
            how_close = arr[i] + arr[right] + arr[left]
            print(how_close)
            if target - how_close < global_closest:
                answer = [arr[i], arr[left], arr[right]]
                global_closest = max(global_closest, target-how_close)
            if arr[left] + arr[right] == needed:
                return [arr[i], arr[left], arr[right]]
            elif arr[left] + arr[right] > target:
                right -= 1
            else:
                left += 1
    return answer



arr = [12, 3, 4, 1, 6, 9]
print(three_sum_closest(arr, 28))
