import unittest

def string_compression(string):

    # Should we assume input will always be a valid string?
    if type(string) != str:
        return 'Error'
    elif string.isalpha() is False:
        return 'Error'

    output = []
    count = 1
    
    for index in range(len(string)-1):
        if string[index+1] == string[index]:
            count += 1
        else:
            output.append(string[index])
            output.append(str(count))
            count = 1

    output.append(string[index])
    output.append(str(count))

    # Return shorter length of original and compressed string
    return min(''.join(output), string, key=len)


class TestSolution(unittest.TestCase):

    def test_long_string(self):
        long_string = 'aabcccccaaa'
        answer = string_compression(long_string)
        self.assertEqual(answer, 'a2b1c5a3')

    def test_short_string(self):
        short_string = 'bac'
        answer = string_compression(short_string)
        self.assertEqual(answer, short_string)
        
    def test_error_string(self):
        error_string = '123'
        answer = string_compression(error_string)
        self.assertEqual(answer, 'Error') 


if __name__ == '__main__':
    unittest.main()
