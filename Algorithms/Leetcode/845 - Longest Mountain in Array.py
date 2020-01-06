class Solution:
    def longestMountain(self, A):
        """
                   e
          s 
        [875, 884, 239, 731, 723, 685]
         0     1    2    3    4    5  
        """
        start, end = 0, 0 
        global_max = 0 
        
        while end + 1 < len(A):
            end = start + 1
            if A[start] > A[end]:
                start += 1
                continue
            while A[end-1] < A[end]:
                end += 1
            while end < len(A) and A[end-1] > A[end]:
                end += 1 
                if end - start >= 3:
                    global_max = max(global_max, end - start)
            
            start +=  1 
            
        return global_max
    
arr =[0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
s = Solution()
print(s.longestMountain(arr))
