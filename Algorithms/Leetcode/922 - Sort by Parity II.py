class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        
        Run Times:
        O(n^2)     
        O(nlogn)
        O(n)
        O(logn)
        O(1)
        
        Solution:
        1. Sort array to have evens infront, odds in back
        2.
        """
    
    def sortArrayByParityII_3(self, A):

        ans = [x for x in range(len(A))]
        even = 0
        odd = 1
        for num in A:
            if num % 2 == 0:
                ans[even] = num
                even += 2
                
        for num_2 in A:
            if num_2 % 2 != 0:
                ans[odd] = num_2
                even += 2
        
        return ans
        
        
    def sortArrayByParityII_2(self, A):
        if len(A) == 0:
            return A
        
        current = 0
        odd = len(A)-1
        while current < odd:
            if A[current] % 2 != 0:
                A[current], A[odd] = A[odd], A[current]
                odd -= 1
            else:
                current += 1
                
                
        low, high = 0, len(A) - 1
        
        A2 = []
        
        for index in range(len(A)): 
            if index % 2 != 0:
                A2.append(A[high])
                high -= 1
            else:
                A2.append(A[low])
                low += 1
                
        return A2
            
            
        
