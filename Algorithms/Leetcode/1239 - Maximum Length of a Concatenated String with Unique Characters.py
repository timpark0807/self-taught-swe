class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int  
        1. Try and store all possible concatentations
        2. Find the maximum length one that's unqiue 
       """
        self.global_max = 0 
        self.backtrack(arr, set(), set(), 0)
        return self.global_max  
        

    def backtrack(self, arr, seen, curr, index):
        self.global_max = max(self.global_max, len(curr))

        for index in range(index, len(arr)):
            if index not in seen and self._isValid(arr[index], curr):
                
                seen.add(index) 
                for letter in arr[index]:
                    curr.add(letter)
                    
                self.backtrack(arr, seen, curr, index+1) 
                
                for letter in arr[index]:
                    curr.remove(letter)
                seen.remove(index) 
                
    def _isValid(self, word, curr):
        temp = set() 
        
        for letter in word:
            if letter in curr or letter in temp:
                return False
            temp.add(letter)
        return True 
    
