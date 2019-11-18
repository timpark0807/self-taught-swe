def moveZerosToEnd(arr):
    i, j = 0, 0

    while j < len(arr):
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]

        if arr[i] != 0:
            i += 1

        j += 1

    return arr

print(moveZerosToEnd([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))

