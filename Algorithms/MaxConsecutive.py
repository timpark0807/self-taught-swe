class Solution:
    def findMaxConsecutiveOnes(self, nums):
        
        """
        Incorrectly tried to do a nested for loop.

        This solution works because it allows us to do 1 pass through the array

        If the num we iterate is not 1:
            -> increment count by 1
            -> check if current count is largest
                -> If current count is largest, set largest to count

        If the num we iterate is not 1
            -> reset the count to 0.

        Return Largest 
        """

        
        if 1 not in nums:
            return 0 
        
        largest = 0
        count = 0 
        
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                if count > largest:
                    largest = count
                    
        return largest

    
