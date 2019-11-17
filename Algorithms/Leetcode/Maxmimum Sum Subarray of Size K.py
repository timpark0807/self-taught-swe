def max_subarray_k(arr, k):
    left, right = 0, k-1
    current_sum = 0
    # set window and current sum

    while k > 0:
        current_sum += arr[k-1]
        k -= 1

    overall_max = current_sum
    
    while right < len(arr) - 1:
        right += 1
        current_sum += arr[right]
        current_sum -= arr[left]
        left += 1
        overall_max = max(overall_max, current_sum)

    return overall_max


print(max_subarray_k([2, 1, 5, 1, 3, 2], 3))
print(max_subarray_k([2, 3, 4, 1, 5], k=2))
