class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = 0 
        for word in words:
            if self.is_good(word, chars):
                count += len(word)
                
        return count
        
    def is_good(self, word, chars):
        
        char_dict = {}
        
        for char in chars:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        for letter in word:
            if letter in char_dict:
                char_dict[letter] -= 1
            else:
                return False
        
        for char in char_dict.values():
            if char < 0:
                return False
            
        return True
            
            
