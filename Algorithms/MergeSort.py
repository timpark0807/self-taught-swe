class MergeSort:
    """
    Mergesort Implementation
    Time  : O(nlogn)
    Space : O(n)
    """
    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left, right = self.mergesort(arr[:mid]), mergesort(arr[mid:])
        return merge(left, right)

    def merge(self, left, right):
        lp, rp = 0, 0
        new_list = []
        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                new_list.append(left[lp])
                lp += 1
            else:
                new_list.append(right[rp])
                rp += 1

        new_list.extend(left[lp:])
        new_list.extend(right[rp:])

        return new_list
