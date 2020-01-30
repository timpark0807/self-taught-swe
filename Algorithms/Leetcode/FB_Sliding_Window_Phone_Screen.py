import unittest

def findMaxVacationLength(year, pto):
    """
    Variables Needed:
    left, right = 0, 0
    global_max = -infinity
    num_F = 0
    
                              r   
                     l 
    year = [F, T, F, T, F, T, F]
            0  1  2  3  4  5  6

    num_F = 2
    
    1. Expand right
        -> if year[right] == 'F'
            -> num_F += 1
        -> right += 1
        
    2. Meet a condition
        -> while num_F > pto:
        
    3. Process the subarray
        -> curr_max = len(year[left:right])
        -> global_max = max(global_max, curr_max)
        
    4. Minimize left
        -> if year[left] == 'F':
            -> num_F -= 1
        -> left += 1
    
    5. return global_max
    
    """
    left, right = 0, 0
    global_max = 0
    count_F = 0

    while right < len(year):
        if year[right] == 'F':
            count_F += 1
        
        while count_F > pto:
            global_max = max(global_max, right-left)
            if year[left] == 'F':
                count_F -= 1
            left += 1
            
        right += 1

    if count_F <= pto:
        global_max = max(global_max, right-left)

    return global_max

"""
                  r 
            l   
    year = [F, F, F, F]
            0  1  2  3  4
            
    pto = 2

global_max = 5
count_F = 2


"""


class Test(unittest.TestCase):
    def test_one(self):
        year = ['F', 'T', 'F', 'T', 'F', 'T', 'F']
        pto = 2
        answer = findMaxVacationLength(year, pto)
        self.assertEqual(answer, 5)

    def test_two(self):
        year = ['F', 'T', 'T', 'T', 'T', 'T', 'F']
        pto = 2
        answer = findMaxVacationLength(year, pto)
        self.assertEqual(answer, 7)
        
    def test_five(self):
        year = ['F', 'T', 'F', 'T', 'T', 'F', 'F']
        pto = 5
        answer = findMaxVacationLength(year, pto)
        self.assertEqual(answer, 7)
        
    def test_three(self):
        year = ['F', 'F', 'F', 'F']
        pto = 2
        answer = findMaxVacationLength(year, pto)
        self.assertEqual(answer, 2)

    def test_four(self):
        year = ['T', 'T', 'T', 'T']
        pto = 2
        answer = findMaxVacationLength(year, pto)
        self.assertEqual(answer, 4)



    
if __name__ == '__main__':
    unittest.main()
