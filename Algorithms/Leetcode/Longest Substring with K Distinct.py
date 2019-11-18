import unittest
import collections

class Solution:

    def longest_substring_with_k_distinct(self, string, k):
        """
                            r
        string = 'a r a a c i'
                  0 1 2 3 4 5
                 0 1 2 3 4 5 6
                      l 

        freq = {a:2,
                c:1,
                
        """
        if string == '':
            return 0
        
        left, right = 0, 0
        overall_max = float('-inf')
        freq = collections.defaultdict(int)

        while right < len(string):
            right_char = string[right]
            freq[right_char] += 1
            right += 1

            while len(freq) > k:
                left_char = string[left]

                curr_substring = string[left:right-1]
                overall_max = max(overall_max, len(curr_substring))
                freq[left_char] -= 1
                if freq[left_char] == 0:
                    del freq[left_char]
                left += 1
                

        return overall_max



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def test_valid(self):
        string = 'araaci'
        k = 2
        answer = self.s.longest_substring_with_k_distinct(string, k)
        self.assertEqual(answer, 4)


    def test_edge_case(self):
        string = ''
        k = 2
        answer = self.s.longest_substring_with_k_distinct(string, k)
        self.assertEqual(answer, 0)

if __name__ == '__main__':
    unittest.main()
    
