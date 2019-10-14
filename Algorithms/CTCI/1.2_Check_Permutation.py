import unittest

class Solution:
    def check_permutations(string1, string2):
        if type(string1) != str and type(string2) != string:
            return False
        elif len(string1) != len(string2):
            return False
        
        freq = {}
        
        for letter in string1:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1

        for letter in string2:
            if letter not in freq:
                return False
            else:
                freq[letter] -= 1
                if freq[letter] < 0:
                    return False

        for value in list(freq.values()):
            if value != 0:
                return False
            
        return True


    def check_permutations_2(string1, string2):
        return sorted(string1) == sorted(string2)


class TestSolution(unittest.TestCase):

    string1 = 'abcdfsd'
    string2 = 'cbaddfs'

    def test_one(self):
        ans = Solution.check_permutations(self.string1, self.string2)
        self.assertTrue(ans)

    def test_two(self):
        ans = Solution.check_permutations_2(self.string1, self.string2)
        self.assertTrue(ans)
        

if __name__ == '__main__':
    unittest.main()
