class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        
        Clarify:
            - Return an array
            - Let's do this out of place first, then in place to save space
            - If len(A) == 1 -> return A
            
        Plan:
            - 2 Pass solution
                -> Iterate through array, if even -> append to auxillary array
                -> Irerate through array, if odd -> append to auxillary array 

        In Place:
            - 1 Pass
                -> while loop with current = 0, hold odd boundary at end of array
                -> if current value is even, current value is in correct place -> move to next element
                    - current += 1
                -> if current value is odd, swap values at current and odd indicies
                    - Decrement odd index by 1 -> moving odd boundary in
                    - Don't increment current, we need to check the value that we just swapped in

               c        o 
        arr = [6, 1, 2, 5]
        current = 0
        odd = 3
        arr[current] = 6
        -> current value is even, increment current

                  c     o
        arr = [6, 1, 2, 5]
        current = 1
        odd = 3
        arr[current] = 1
        -> current value is odd, swap current and odd boundary index
        -> decrement odd index
        
                  c  o   
        arr = [6, 5, 2, 1]
        current = 1
        odd = 2
        arr[current] = 5
        -> current value was not incremented after swap, we need to check the value we swapped is even or odd
        -> current value is odd, swap current and odd values again and decrement odd index

                  o 
                  c
        arr = [6, 2, 5, 1]
        current = 1
        odd = 1
        -> while loop beraks, array is sorted by evens and odds

        """
         
        if len(A) <= 1:
            return A       
        
        current = 0
        odd = len(A)-1
        
        while current < odd:
            if A[current] % 2 == 0:
                current += 1
            if A[current] % 2 != 0:
                A[current], A[odd] = A[odd], A[current]
                odd -= 1 
                
        return A 
        
        
    def sortArrayByParity_outofplace(self, A):

        answer = []
        
        if len(A) <= 1:
            return A
        
        for num in A:
            if num % 2 == 0:
                answer.append(num)
        
        for num in A: 
            if num % 2 != 0:
                answer.append(num)
        
        return answer
        
