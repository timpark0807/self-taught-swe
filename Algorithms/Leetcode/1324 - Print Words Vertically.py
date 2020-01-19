class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        
        
        s = "HOW ARE YOU"
        
        
        words = ['HOW', 'ARE', 'YOU']
                   ^      ^      ^
          
        ['HAY', 'ORO', 'WEU' ]
          
        ['CONTEST', 'IS', 'COMING']
             ^          ^     ^
        
        ['CIC',
         'OSO',
         'N_M'
         'T_I']
         'T__P'
         # Step 1. Convert string to list of stirngs
         # Step 2. Find max length of a word 
         # Step 3. For index in range(max_word_length)
                    # temp_word = ''
            # Step 4. For word in words
                # Check if index is valid for the word
                    # If is, append letter
                    # If not, append ' '
        """
        words = s.split(' ')
        longest_word = max(words, key=len)
        retval = []
        
        for index in range(len(longest_word)):
            temp_arr = []
            for word in words:
                if index < len(word):
                    temp_arr.append(word[index])
                else:
                    temp_arr.append(' ')
            
            for letter in temp_arr[::-1]:
                if letter == ' ':
                    temp_arr.pop()
                else:
                    break
                    
            temp_word = ''.join(temp_arr) 
            retval.append(temp_word)
            
        return retval 
        
