import unittest

class Solution:

    def reverse(self, string):
        # Time  :  O(n)
        # Space :  O(n)
        # Where n is the number of words in the string
        
        # string to array
        arr_string = string.split(" ")
        output = []
        
        # [3, 2, 1, 0]
        for index in reversed(range(len(arr_string))):
            output.append(arr_string[index])

        return " ".join(output)


    def reverse_inplace(self, string):
        arr_string = string.split(" ")
        low = 0
        high = len(arr_string) -1

        while low < high:
            self.swap(arr_string, low, high)
            low += 1
            high -= 1

        return " ".join(arr_string)


    def swap(self, item, low, high):
        item[low], item[high] = item[high], item[low]
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s  = None

    def test_easy_string(self):
        string = 'the sky is blue'
        answer = self.s.reverse(string)
        self.assertEqual(answer, 'blue is sky the')

    def test_inplace(self):
        string = 'the sky is red'
        answer = self.s.reverse_inplace(string)
        self.assertEqual(answer, 'red is sky the')


if __name__ == '__main__':
    unittest.main()
