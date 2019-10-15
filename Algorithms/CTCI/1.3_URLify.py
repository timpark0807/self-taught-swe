import unittest

def URLify(url):
    spaces = count_spaces(url)
    end_of_word_index = len(url) - (spaces * 2) - 1
    boundary = len(url) - 1
    url = list(url)
    
    while end_of_word_index < boundary:
        if url[end_of_word_index].isalpha():
            url[end_of_word_index], url[boundary] = url[boundary], url[end_of_word_index]
            boundary -= 1
            
        elif url[end_of_word_index] == ' ':
            url[boundary] = '0'
            url[boundary - 1] = '2'
            url[boundary - 2] = '%'
            boundary -= 3
            
        end_of_word_index -= 1

    return ''.join(url)

def count_spaces(url):
    spaces = 0
    for letter in url:
        if letter == ' ':
            spaces += 1
            
    return spaces // 3



class TestSolution(unittest.TestCase):

    def test_spaces(self):
        url_spaces = "Mr John Smith    "
        ans = URLify(url_spaces)
        self.assertEqual(ans, "Mr%20John%20Smith")

    def test_no_spaces(self):
        url_no_spaces = "MrJohnSmith"
        ans = URLify(url_no_spaces)
        print(ans)
        self.assertEqual(ans, "MrJohnSmith")

if __name__ == '__main__':
    unittest.main()

