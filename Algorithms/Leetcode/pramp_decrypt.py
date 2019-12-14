import unittest

def decrypt(word):

  if len(word) == 0:
    return ''

  # Step 0: Preprocess
  temp = list(word)
  
  # Step 1: Get letters in ASCII
  for index, letter in enumerate(temp):
    temp[index] = ord(letter)
  
  # Step 2: Subtract 1 to first letter
  temp[0] -= 1
  
  # Step 3: Subtract value of prev to curr
  for index in range(1, len(temp)):
    temp[index] -= ord(word[index-1])
    
    # Step 4: Add 26 until we are in range 97 - 122 
    while temp[index] < 97:
      temp[index] += 26
      
  for index, ascii_letter in enumerate(temp):
    temp[index] = chr(ascii_letter)
  # Step 5: Convert temp list back to string and return
  answer = ''.join(temp)
  return answer
 
  
  """
  Embrace challenge
  Embrace Ambiguity
  
  
  d    n   o   t   q 
  100 110 111 116 113
      
      -99
      
      +26
      +26
      +26
  
  c
  99  
  
  Decrypted
  1. r += c 
  2. c -= 26 until we're in range
  Encrypted
 
 
  100	214	319	428	529
 
  """

class TestSolution(unittest.TestCase):
  def test_one(self):
    word = "dnotq"
    self.assertEqual(decrypt(word), 'crime')
    
  def test_edgecase(self):
    word = ''
    self.assertEqual(decrypt(word), '')
    
if __name__ == '__main__':
  unittest.main()
"""
  Input: string 
  Output: string
    -> ** I'll change the input to a list, but have to convert the list back to a string before returning
        -> temp = list(word)
        -> temp = ''.join(temp)

  Brute Force:
    -> Time: O(n)
    -> Space: O(n)
      -> We can optimize O(1) space 
      
  Assumptions:
    -> lowercase letters 
    -> No spaces, no punctutation, only valid lowercase letters
  
  Edge Cases: 
    -> empty word
    
  TestCases:
    -> 

  
  0. Preprocess -> convert string to list of letters
  
          word = "dnotq"
          temp = ['d', 'n', 'o', 't','q']
  
  
  1. Get letters ASCII value 
    -> loop through temp, convert that to ascii
      ****** Look up python function
    
              d    n    o    t    q
      temp = [99, 114, 105, 109, 101]
    
    
  2. If it is the first letter, just add 1 
      
      temp[0] += 1

      temp = [100, 114, 105, 109, 101]
               ^
               +=1 
    
    
  3. For every letter after first, add value of prev 
      
      
    -> Loop through 2nd to last ascii values
       
       -> for index in range(1, len(temp)):

    -> Add temp[index] += temp[index-1] 
    
    Before:
        temp = [100, 114, 105, 109, 101]

    After: 
        temp = [100, 214, 319, 428, 529]


  4. Subtract "After" temp by 26 UNTIL we are in lowercase ascii range
    -> ******What is lowercase ascii range?
  
  
  5. Convert ascii to letters
    -> ******What is ascii -> letter function
    
"""




