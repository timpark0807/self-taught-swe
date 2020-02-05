class QuickSort:
    """
    Quicksort Implementation
    Time  : O(nlogn)
    Space : O(logn) <- recursive stack frame 
    """
    def quicksort(self, arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            self.quicksort(arr, low, p-1)
            self.quicksort(arr, p+1, high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[high]
        boundary = low

        for index in range(low, high):
            if arr[index] < pivot:
                arr[index], arr[boundary] = arr[boundary], arr[index]
                boundary += 1

        arr[boundary], arr[high] = arr[high], arr[boundary]

        return boundary

