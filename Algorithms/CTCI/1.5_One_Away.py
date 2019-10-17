import unittest

class Solution:

    def one_away(self, string1, string2):
        
        if len(string1) - len(string2) > 1:
            return False

        pointer_1 = 0
        pointer_2 = 0
        diff = 0
        
        while pointer_1 < len(string1) and pointer_2 < len(string2):
            if string1[pointer_1] != string2[pointer_2]:
                
                diff += 1

                if diff > 1:
                    return False
                
                # Edit string 1 or 2
                if string1[pointer_1 + 1] == string2[pointer_2 + 1]:
                    pointer_1 += 1
                    pointer_2 += 1

                # Delete from string 1 
                elif string1[pointer_1 + 1] == string2[pointer_2]:
                    pointer_1 += 1

                # Delete from string 2
                elif string1[pointer_1] == string2[pointer_2 + 1]:
                    pointer_2 += 1

            else:
                pointer_1 += 1
                pointer_2 += 1

        if diff > 0 and (pointer_1 < len(string1) or pointer_2 < len(string2)):
            return False
        
        return diff <= 1


class TestSolution(unittest.TestCase):

    def test_valid_one_delete(self):
        s = Solution()
        self.assertEqual(s.one_away('pale', 'ale'), True)
        self.assertEqual(s.one_away('pales', 'pale'), True)
        self.assertEqual(s.one_away('pale', 'bale'), True)
        self.assertEqual(s.one_away('pale', 'bake'), False)
        self.assertEqual(s.one_away('ale', 'pale'), True)
        self.assertEqual(s.one_away('aale', 'ale'), True)
        self.assertEqual(s.one_away('aael', 'ale'), False)
        self.assertEqual(s.one_away('motherinlaw', 'wxmanhitler'), False)
        self.assertEqual(s.one_away('motherinlaw','motherinlow'), True)


if __name__ == '__main__':
    unittest.main()

