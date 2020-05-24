class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
             l 
        s = "a b c i i i d e f"
             0 1 2 3 4 5 6 7 8
                       r
             
        k = 3
        
        cv = 2
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}

        left, right = 0, k
        currVowels = 0
        for index in range(k):
            if s[index] in vowels:
                currVowels += 1
        globalMax = currVowels
        
        while right < len(s): 
            rightChar = s[right] 
            leftChar = s[left]
            if rightChar in vowels:
                currVowels += 1
            if leftChar in vowels:
                currVowels -= 1  
            globalMax = max(globalMax, currVowels) 
            left += 1
            right += 1
        
        
        return globalMax 
