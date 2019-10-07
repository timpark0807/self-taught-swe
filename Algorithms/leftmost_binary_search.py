def leftmost(arr, target, direction):
    low = 0
    high = len(arr)
    result = 0
    while low < high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            result = mid
            if direction == 'left':
                high = mid-1
            else:
                low = mid +1
                
    return result

if __name__ == '__main__':
    arr = [1, 2, 3, 5, 6, 6, 6, 7]
    ans = leftmost(arr, 6, 'left')
    print(ans)
