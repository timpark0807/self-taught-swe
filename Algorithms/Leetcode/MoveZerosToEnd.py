def moveZerosToEnd(arr):
    boundary, current = 0, 0

    while current < len(arr):
        if arr[boundary] == 0 and arr[current] != 0:
            arr[boundary], arr[current] = arr[current], arr[boundary]

        if arr[boundary] != 0:
            boundary += 1

        current += 1

    return arr

print(moveZerosToEnd([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))

