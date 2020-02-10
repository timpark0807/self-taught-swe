import collections

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        
        Optimization Problem
    
        
        l : 1 
        e : 3
        t : 1
        c : 1
        o : 1
        d : 1
        
        t = "practice"
        
        p : 1
        r : 1
        a : 1
        c : 2
        t : 1
        i : 1
        e : 1
                  
                  
        ans = p -> 1, r -> 1, a -> 1, c -> 1, i -> 1 
            only 
        
        # Get counts of both s and t 
        
        # For letter and count in t 
            If that letter does not exist in s 
                ans += freq_t[letter]
            elif if freq_t[letter] > freq_s[letter]
                ans += freq_t[letter] - freq_s[letter] 
        
        """
        
        freq_s = self.get_count(s)
        freq_t = self.get_count(t)
        
        ans = 0
        for letter, count in freq_t.items():
            if letter not in freq_s:
                ans += freq_t[letter]
            elif freq_t[letter] > freq_s[letter]:
                ans += freq_t[letter] - freq_s[letter]
        return ans
    
    def get_count(self, string):
        freq = collections.defaultdict(int)
        for letter in string:
            freq[letter] += 1
        return freq 
        
        
        
        
