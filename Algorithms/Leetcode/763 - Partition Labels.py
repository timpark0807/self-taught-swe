class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        
                         r 
        "a b a b c b a c a d e f e g d e h i j h k l i j"
         0 1 2 3 4 5 6 7 8 9 10
         l                 
         
        curr = a:1, b 
        
        a : 3 
        b : 2 
        c : 2 
        d : 2 
        e : 2
        g : 1 
        h : 1 
        i : 2 
        
        
        get a count of all the letters 
        
        do a sliding window
        keep track of the current letters we have in our window and our count 
        expand until all the letters in our window have been compeletley seen
        reset the left pointer 
        
        """

        counts = collections.defaultdict(int) 
        
        for letter in S:
            counts[letter] += 1
        
        curr = collections.defaultdict(int)         
        left, right = 0, 0
        answer = [] 
        
        while right < len(S):
            curr[S[right]] += 1
            right += 1
            if self._isValid(curr, counts):
                answer.append(right-left)  # todo: check off by 1 
                left = right 


        return answer 
        
    def _isValid(self, curr, counts):
        for letter, count in curr.items():
            if count != counts[letter]:
                return False
        return True 
    
     
