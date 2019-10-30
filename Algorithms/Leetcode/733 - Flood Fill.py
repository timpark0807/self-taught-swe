import unittest

class Solution:
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        seen = set()
        self.bfs(image, seen, sr, sc, oldColor, newColor)
        return image

    def bfs(self, image, seen, row, col, oldColor, newColor):
        if (row, col) not in seen:
            seen.add((row, col))

            if row < 0 or row >= len(image):
                return 0
            if col < 0 or col >= len(image[row]):
                return 0

            if image[row][col] == oldColor:
                for i in image:
                    print(i)
                print('*'*30)
                
                image[row][col] = newColor
                
                # up, down, right, left
                self.bfs(image, seen, row - 1, col, oldColor, newColor)
                self.bfs(image, seen, row + 1, col, oldColor, newColor)
                self.bfs(image, seen, row, col + 1, oldColor, newColor)
                self.bfs(image, seen, row, col - 1, oldColor, newColor)

        return 0 


class Test(unittest.TestCase):
    def test_valid(self):
        s = Solution()
        image = [[1,1,1],
                 [1,1,0],
                 [1,0,1]]
        
        output = [[2,2,2],[2,2,0],[2,0,1]]
        answer = s.floodFill(image, 1, 1, 2)
        self.assertEqual(output, answer)


"""
***********
[1, 1, 1]
[1, 1, 0]
[1, 0, 1]
***********
[1, 1, 1]
[1, 2, 0]
[1, 0, 1]
***********
[1, 2, 1]
[1, 2, 0]
[1, 0, 1]
***********
[1, 2, 2]
[1, 2, 0]
[1, 0, 1]
***********
[2, 2, 2]
[1, 2, 0]
[1, 0, 1]
***********
[2, 2, 2]
[2, 2, 0]
[1, 0, 1]
***********
[2, 2, 2]
[2, 2, 0]
[2, 0, 1]
***********
"""
if __name__ == '__main__':
    unittest.main()



