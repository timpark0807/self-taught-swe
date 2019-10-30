import unittest

class Solution:

    def bfs(self, matrix, startrow, startcol, endrow, endcol):
        queue = [(startrow, startcol)]
        seen = set()
        backtrack = { matrix[startrow][startcol] : None }
        while queue:
            current = queue.pop(0)
            x = current[0]
            y = current[1]
            if (x,y) not in seen:
                seen.add((x,y))
                if (x, y) == (endrow, endcol):
                    count = 0
                    value = matrix[current[0]][current[1]]
                    while value is not None:
                        count += 1
                        value = backtrack[value]

                    return count - 1
                
                    matrix[x][y]
                for adj in [(0,1),(1,0),(0,-1),(-1,0)]:
                    v = (x+adj[0], y + adj[1])
                    vrow = v[0]
                    vcol = v[1]
                    if (vrow >= 0 and vrow < len(matrix)) and (vcol >= 0 and vcol < len(matrix[0])) and matrix[vrow][vcol] != 0:
                        if v not in seen:
                            queue.append(v)
                            backtrack[matrix[vrow][vcol]] = matrix[x][y]
                            print(queue)
                            print(backtrack)

        return None
    
class Test(unittest.TestCase):
    def test_forest_valid(self):
        forest = [[5,4,3],
                  [0,0,2],
                  [0,0,0]]
        s = Solution()
        answer = s.bfs(forest, 0, 0, 1, 2)
        self.assertEqual(answer, 3)

if __name__ == '__main__':
    unittest.main()
