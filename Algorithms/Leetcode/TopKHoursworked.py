import heapq
import unittest
import collections

def top_k(tup, k):
    heap = []
    d = collections.defaultdict(int)
    
    for worker_id, num_hours in tup:
        d[worker_id] += num_hours
    for worker_id, num_hours in d.items():
        heapq.heappush(heap, (-num_hours, worker_id))
        
    res = []
    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1
        
    return res

class TestSolution(unittest.TestCase):
    def test_solution(self):
        tup = [(1, 30), (2, 20), (1, 40), (3, 10)]
        k = 2
        ans = top_k(tup, k)
        self.assertEqual(ans, [1,2])

if __name__ == '__main__':
    unittest.main()
