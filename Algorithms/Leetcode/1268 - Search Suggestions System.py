class Solution:
    def suggestedProducts(self, products, searchWord):
        """
        Description: Suggests up to 3 words in relation to each letter of the search word 
        
        @param products : arr[str]
        @param searchWord : str
        @return : arr[arr[str]]

        Return: 
                - outer array length == length of searchWord
                - inner array length <= 3 

        
        # Step 0: 
            - Sort the products
            
        # Step 1: 
            - Build a trie
                - Standard trie but inside every trie hold an array of words that pass through 
        
        # Step 2: 
            - Iterate through the letters of the searchWord
                - Move into the current trie of that letter
                - Check the words that are apart of that three and return the top 3
                
        """
        
        trie = self._get_trie(products)
        retval = [] 
        index = 0
        for letter in searchWord:
            if letter not in trie:
                break
            curr_words = trie['word_arr'][:3]
            trie = trie[letter]
            retval.append(curr_words)
            index += 1
            
        retval.append(trie['word_arr'][:3])
        while index < len(searchWord):
            retval.append([])
            index += 1
        
        return retval[1:]
    
    def _get_trie(self, products):
        trie = {'word_arr':[]}
        products.sort()
        for product in products:
            curr_trie = trie 
            for letter in product:
                if letter not in curr_trie:
                    curr_trie[letter] = {}

                curr_trie = curr_trie[letter]
                if 'word_arr' not in curr_trie:
                    curr_trie['word_arr'] = []
                curr_trie['word_arr'].append(product)
        return trie 
    
    
    
s = Solution()
print(s.suggestedProducts(["bags","baggage","banner","box","cloths"],"bags"))
    
s = Solution()
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
    
     
print(s.suggestedProducts(products = ["havana"], searchWord = "tatiana"))
    
    
    
    
    
    
    
    
    
    
    
    
    
