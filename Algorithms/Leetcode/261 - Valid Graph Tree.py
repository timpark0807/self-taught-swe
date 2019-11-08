import unittest
import collections

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        adj_list = self.get_adj_list(edges)

        queue = [0]
        seen = set([0])

        while queue:
            current = queue.pop(0)
            for neighbor in adj_list[current]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
                elif neighbor in seen:
                    return False
    
        return True

    def get_adj_list(self, edges):
        adj_list = collections.defaultdict(list)

        for x, y in edges:
            adj_list[x].append(y)
            
        return adj_list


class TestSolution(unittest.TestCase):

    def test_valid_tree(self):
        n = 5
        valid_edges = [[0,1],
                     [0,2],
                     [0,3],
                     [1,4]]
        s = Solution()
        valid_answer = s.validTree(n, valid_edges)
        self.assertTrue(valid_answer)
        
    def test_invalid_tree(self):
        n = 5
        invalid_edges = [
                        [0,1],
                        [1,2],
                        [2,3],
                        [1,3],
                        [1,4]]
        s = Solution()
        invalid_answer = s.validTree(n, invalid_edges)
        self.assertFalse(invalid_answer)

if __name__ == '__main__':
    unittest.main()
