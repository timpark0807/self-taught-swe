import unittest
import unittest

def num_of_islands(islands):
    seen = set()
    count = 0 
    for row in range(len(islands)):
        for col in range(len(islands[row])):
            if (row, col) not in seen and islands[row][col] == 1:
                count += bfs(islands, row, col, seen)
    return count

def bfs(islands, row, col, seen):
    if (row, col) not in seen:
        seen.add((row, col))
        
        if row < 0 or row >= len(islands):
            return 0

        if col < 0 or col >= len(islands[row]):
            return 0

        if islands[row][col] == 1:
            
            bfs(islands, row + 1, col, seen)
            bfs(islands, row - 1, col, seen)
            bfs(islands, row, col + 1, seen)
            bfs(islands, row, col - 1, seen)
            
            return 1
        
    return 0

class Test(unittest.TestCase):
    def test_valid(self):
        islands = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
            ]
        answer = num_of_islands(islands)
        self.assertEqual(answer, 3)

if __name__ == '__main__':
    unittest.main()
