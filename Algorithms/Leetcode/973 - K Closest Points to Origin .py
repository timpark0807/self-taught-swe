import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if points == []:
            return []
        if len(points) == 1:
            return points[0]
        
        heap = [] 
        
        for point in points:
            distance = point[0]**2 + point[1]**2 
            heapq.heappush(heap, (distance, point))
            
        answer = []
        
        for iteration in range(K):
            ans = heapq.heappop(heap)
            answer.append(ans[1])
            
        return answer


if __name__ == '__main__':
    s = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    K = 2

    ans = s.kClosest(points, K)
    print(ans)
