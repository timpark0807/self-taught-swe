import unittest

def integer_to_english(n):
    chunks = getChunks(n)
    stringChunks = getStringChunks(chunks)
    answer = seperator(stringChunks)
    return answer 

def getChunks(n):
    # returns a list of strings 
    stack = [num for num in str(n)]
    chunks = []
    while stack:
        curr = [] 
        for _ in range(3):
            if not stack:
                break
            curr.append(stack.pop())
        chunks.append(''.join(reversed(curr)))
    return chunks[::-1]

def getStringChunks(chunks):
    # to do handle teens
    # '15' -> fifteen
    ones = {'0':'',
            '1':'one',  '2':'two',  '3':'three',
            '4':'four', '5':'five', '6':'six',
            '7':'seven','8':'eight','9':'nine'}
    tens = {'1':'ten',    '2':'twenty', '3':'thirty',
            '4':'fourty', '5':'fifty',  '6':'sixty',
            '7':'seventy','8':'eighty', '9':'ninety'} 
    teens = {'10':'ten', '11':'eleven', '12':'twelve',
             '13':'thirteen', '14':'fourteen', '15':'fifteen',
             '16':'sixteen', '17':'seventeen', '18':'eighteen',
             '19':'nineteen'}
    
    stringChunks = []

    for chunk in chunks:
        currChunk = []
        
        if len(chunk) == 3:
            currChunk.append(ones[chunk[0]])
            currChunk.append('hundred')
            chunk = chunk[1:]
            
        if len(chunk) == 2 and chunk[0] == '1':
            currChunk.append(teens[chunk])
            chunk = chunk[2:] 
        elif len(chunk) == 2: 
            currChunk.append(tens[chunk[0]])
            chunk = chunk[1:]
            
        if chunk:
            currChunk.append(ones[chunk[0]])
            
        stringChunks.append(' '.join(currChunk)) 

    return stringChunks


def seperator(stringChunks):
    sep = ['billion', 'million', 'thousand']
    if len(stringChunks) == 4:
        start = 0
    if len(stringChunks) == 3:
        start = 1
    if len(stringChunks) == 2:
        start = 2
    if len(stringChunks) == 1:
        start = 3
        
    answer = [] 
    for index in range(len(stringChunks)):
        answer.append(stringChunks[index])
        if start < len(sep):
            answer.append(sep[start])
            start += 1
            
    return ' '.join(answer) 
        


"""
asnswer = [64, billion, 534, million, 550, thousand, 3895]
index = 0

['534', '550', '375']
                 ^

['billion', 'million', 'thousand']
               s
 
     
if len(stringChunks) == 3:
    need to start with million

if len(stringChunks) == 2:
    need to start with thousand
    

75
 ^
sc = [three hundred seventy five

'5'

'55'

'05'
 ^

five hundred fifty five 

          

'550375'
^
s = [5, 5, 0, 3, 
              ^
curr = [5, 7, 3]
        [3, 7, 5]

chunk = 375

assumptions
    - how big will our number be ?
    - negatives ?
    - integer not float
    
Approach
- Break down n into chunks of 3

- Get the string for each chunk

- insert our number seperators (e.g.: thousand, millions, etc.) 

"""


class TestSolution(unittest.TestCase):
    def test_chunks(self):
        chunk = getChunks(551375)
        expected = ['551', '375']
        self.assertEqual(chunk, expected)
        
        chunk = getChunks(74315)
        expected = ['74', '315']
        self.assertEqual(chunk, expected)

    def test_string_chunks(self):
        stringChunk = getStringChunks(['551', '375'])
        expected = ['five hundred fifty one', 'three hundred seventy five']
        self.assertEqual(stringChunk, expected)
        
        chunk = getStringChunks(['74', '315'])
        expected = ['seventy four', 'three hundred fifteen']
        self.assertEqual(chunk, expected)

    def test_seperator(self):
        answer = seperator(['five hundred fifty one', 'three hundred seventy five'])
        expected = 'five hundred fifty one thousand three hundred seventy five'
        self.assertEqual(answer, expected)

        answer = seperator(['seventy four', 'five hundred fifty one', 'three hundred seventy five'])
        expected = 'seventy four million five hundred fifty one thousand three hundred seventy five'
        self.assertEqual(answer, expected)
        
    def test_one(self):
        answer = integer_to_english(551)
        expected = 'five hundred fifty one'
        self.assertEqual(answer, expected)

    def test_two(self):
        answer = integer_to_english(375)
        expected = 'three hundred seventy five'
        self.assertEqual(answer, expected)

    def test_three(self):
        answer = integer_to_english(551375)
        expected = 'five hundred fifty one thousand three hundred seventy five'
        self.assertEqual(answer, expected)

if __name__ == '__main__':
    unittest.main() 

