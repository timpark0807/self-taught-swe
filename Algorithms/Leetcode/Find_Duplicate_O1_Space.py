import unittest


def find_duplicate(int_list):

    # Find a number that appears more than once ... in O(n) time
    for position in range(0, len(int_list)):
        valueth = abs(int_list[position])
        
        if int_list[valueth] < 0:
            return valueth 
        else:
            int_list[valueth] = -int_list[valueth]
        
    return 0



# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
