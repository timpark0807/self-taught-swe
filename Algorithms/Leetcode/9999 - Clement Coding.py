import unittest

def solve(phoneNumber, words):
    """
    @desc Determines which words are contained in the phone number
    @param1 phoneNumber : str
    @param2 words : str[]
    @return answer : str[]
    """
    
    mapping = {'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':3,
               'g':4, 'h':4, 'i':4, 'j':5, 'k':5, 'l':5,
               'm':6, 'n':6, 'o':6, 'p':7, 'q':7, 'r':7, 's':7,
               't':8, 'u':8, 'v':8, 'w':9, 'x':9, 'y':9, 'z':9}
    
    answer = []
    for word in words:   # O(n)
        
        currMapping = []
        
        for letter in word:   # O(m) 
            currMapping.append(str(mapping[letter]))
            
        serial = ''.join(currMapping)
        if len(serial) <= len(phoneNumber) and serial in phoneNumber: 
            answer.append(word)
            
    answer.sort()
    return answer


class TestSolution(unittest.TestCase):
    def test_one(self):
        ans = solve('3662277', ['foo', 'bar', 'baz', 'foobar', 'emo', 'cap', 'car', 'cat']) 
        self.assertEqual(ans, ['bar', 'cap', 'car', 'emo', 'foo', 'foobar'])

if __name__ == '__main__':
    unittest.main()
    
"""
2 inputs
phone number
list of words



High Level Approach

    Iterate word in words
        Conver the word into it's digit mapping
        Check if that digit mapping is contained in phoneNumber
        
    
"""
