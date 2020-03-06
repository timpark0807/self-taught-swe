"""
Goal: Produce an array with the top N hottest toys

@param numToys   : int
@param topTops   : int
@param toys      : int
@param numQuotes : int
@param quotes    : arr[str]
@return answer   : arr[str]

Note: Length of answer <= topToys

- hashtable <- 'count'
    - key = toys
    - word_count = count of total words seen
    
- hashtable
    - key = toys
    - value = count of sentences the word is in
    
- heap <- top N
    - containing tuples of (word_count, sentence_count, word)
    - Pop off top N

Variables Needed:
    - word hashtable
    - sentence hashtable
    - temporary sentence set
    - toys to a toys_set
    - heap
    - output array
    
# Step 1: Preprocessing
    - Break the quotes into an array of strs 
    - Note that "Elsa!" needs to equal "Elsa"
    - Make all the characters lowercase 
    
# Step 2: Processing
    - Iterate over the sentences
        - Reset the temporary set
        - Iterate over the words in the current sentence
            - If the current word is in toys
            - Increment the count of the word
            - Add the word to the temporary set
        - Iterate over the temporary set
            - Increment the sentence count of that toy
            
# Step 3: Postprocessing
    - Iterate over the toys
    - Add the (count of word, count of setnences, word) to heap
    - Remove the top N of these words
    - Return an array containing only the word 
"""
import unittest
import heapq 

def top_N_toys(numToys, topToys, toys, numQuotes, quotes):
    """
    Description: Returns an array with the top N hottest toys
                 Sorted by frequency of words and in sentences, respectively. 

    @param numToys   : int
    @param topTops   : int
    @param toys      : int
    @param numQuotes : int
    @param quotes    : arr[str]
    @return answer   : arr[str]
    """
    word_hash = {i:0 for i in toys}
    sentence_hash = {i:0 for i in toys}
    
    # Preprocess
    # Time: O(n)
    # Space: O(n)
    # Where n is number of quotes
    processed_quotes = []
    for quote in quotes:
        processed_quotes.append(quote.lower().split())

    # Process
    # Time: O(nm)
    # Space: O(n)
    # Where n is the number of quotes and m is the average length of quotes
    for processed_quote in processed_quotes:
        temp_set = set()
        for word in processed_quote:
            if word in word_hash:
                word_hash[word] += 1
                temp_set.add(word)
        for seen_word in temp_set:
            sentence_hash[seen_word] += 1
    

    # Postprocess
    # Time: O(tlogk)
    # Space: O(k)
    # Where t is the number of toys and k is the top_Toys
    heap = []
    for toy in toys:
        heap_tuple = (word_hash[toy], sentence_hash[toy], toy)
        heapq.heappush(heap, heap_tuple)
        if len(heap) > topToys:
            heapq.heappop(heap)
    
    return [toy for word, sentence, toy in heap[::-1]]
    

class TestSolution(unittest.TestCase):
    def test_one(self):
        numToys = 6
        topToys = 2
        toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
        numQuotes = 6
        quotes = [
        "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
        "The new Elmo dolls are super high quality",
        "Expect the Elsa dolls to be very popular this year, Elsa",
        "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
        "For parents of older kids, look into buying them a drone",
        "Warcraft is slowly rising in popularity ahead of the holiday season"
        ]
        self.assertEqual(top_N_toys(numToys, topToys, toys, numQuotes, quotes), ["elmo", "elsa"])

if __name__ == '__main__':
    unittest.main()
