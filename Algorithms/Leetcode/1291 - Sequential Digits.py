class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        answer = []
        
        self.backtrack(low, high, 0, answer, -1)
        answer.sort() 
        return answer
    
    
    def backtrack(self, low, high, curr, answer, last):
        if low <= curr <= high: 
            answer.append(curr) 
        elif curr > high:
            return 

        for num in range(1, 10):
            if last == -1 or num == last + 1:
                curr *= 10 
                curr += num
                self.backtrack(low, high, curr, answer, num)
                curr -= num
                curr //= 10 
