# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        
        1. Binary Search to find the right most bound
            - log n 
            
            - set left = -9999, right = 9999
                - get a mid point 
                - if the mid point is inbound:
                    - save the answer 
                    - left = mid+1
                - else:
                    - right = mid - 1

                
        2. Binary search to check if the target exists 
            - log n
        """
        
        left, right = 0, self.getRight(reader)
        
        while left <= right:
            mid = (left+right)//2
            curr = reader.get(mid)
            if curr == target:
                return mid 
            elif curr > target:
                right = mid - 1 
            else:
                left = mid + 1
            
        return -1 
        
        
    def getRight(self, reader):
        left = 0 
        right = 20000
        answer = 0 
        
        while left <= right:
            mid = (left+right)//2
            if reader.get(mid) != 2147483647:
                answer = mid 
                left = mid + 1
            else:
                right = mid - 1 
        
        return answer
