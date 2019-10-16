import unittest

def palindrome_permutation(string):
    string = string.lower()
    string = string.replace(' ', '')
    
    if type(string) != str:
        return False
    if len(string) == 0:
        return False
    
    freq = {}
    
    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    check = list(freq.values())
    # If even,
    if len(string) % 2 == 0:
        for value in check:
            if value % 2 != 0:
                return False
    else:
        # If odd
        count_of_odd = 0
        for value in check:
            if value % 2 != 0:
                count_of_odd += 1
            if count_of_odd > 1:
                return False
            
    return True


class TestSolution(unittest.TestCase):

    def test_valid_palindrome_permutation(self):
        valid_string = "ecarrac"
        answer = palindrome_permutation(valid_string)
        self.assertTrue(answer)

    def test_valid_space_palindrome_permutation(self):
        valid_space_string = "tact coa"
        answer = palindrome_permutation(valid_space_string)
        self.assertTrue(answer)

    def test_invalid_palindrome_permutation(self):
        invalid_string = 'notapaliperm'
        answer = palindrome_permutation(invalid_string)
        self.assertFalse(answer)

    def test_empty_palindrome_permutation(self):
        empty_string = ''
        answer = palindrome_permutation(empty_string)
        self.assertFalse(answer)


if __name__ == '__main__':
    unittest.main()
