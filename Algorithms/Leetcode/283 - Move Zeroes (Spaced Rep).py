
def move_zeroes(arr):
    """
    Given an array nums, write a function to move all 0's
    to the end of it while maintaining the relative order
    of the non-zero elements.

    Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    """

    if arr == []:
        return []

    slow, fast = 0, 0

    while fast < len(arr):
        if arr[fast] != 0:
            arr[fast], arr[slow] = arr[slow], arr[fast]
            slow += 1

        fast += 1

    return arr

arr = [0,1,0,3,12]
ans = move_zeroes(arr)
print(ans)

        

