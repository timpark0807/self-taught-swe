class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        result = {}
        answer = [] 

        # Create a dictionary containing the number of
        # times each number appears in nums1
        for num1 in nums1:
            if num1 in result:
                result[num1] += 1
            else:
                result[num1] = 1

        # Iterate through nums2 
        for num2 in nums2:

            # Append the current number to result IF number
            #    1. Appears in the dictionary
            #    2. Has a count greater than 1  
            if num2 in result and result[num2] > 0:
                answer.append(num2)
                result[num2] -= 1
                
                # Decrement the count of the number in the dictionary after appending:
                #
                # Test Case:
                #   nums1 = [0, 2, 4, 2, 7]
                #   nums2 = [2, 2, 2 ,2, 2]
                
                # Explanation:
                #   The number '2' appears in nums1 twice and nums2 five times.
                #   Decrementing count in the dictionary 
                #   prevents us from appending '2' more times than it appears in nums1.

        
        return answer
                
