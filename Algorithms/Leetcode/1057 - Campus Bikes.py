import heapq

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        
                     v
        workers = [[0,0],[1,1],[2,0]]
                     0     1     2 
        
        bikes =   [[1,0],[2,2],[2,1]]
                     0     1     2 
                     ^
                     
        # Add all combinations to a heap 
            # (distance, (worker, bike))
            
        # Pop min off heap
            # curr_distance, curr_worker, curr_bike
            # While curr_distance == heap[0]:   
                # Pop from heap and check and keep the smaller worker
                # Add the bigger worker back to the heap
                # If smaller worker == checked worker:
                    # Keep the smaller bike 
                    # Add other pair back to the heap
                
            # If the ans[curr_worker] == -1 and curr_bike isnt used: 
                # Give curr_worker the curr_bike 
                # add curr_bike to used bikes
                
        return answer 
        
        
        heap : (1, (0, 0))
        
                 0 : 0 : 1 take
                     1 : 4
                     2 : 3
                       
                 1 : 0 : 1 del
                     1 : 2
                     2 : 1 take
                     
                 2 : 0 : 1 del
                     1 : 2 take
                     2 : 1 del 
                

       |
       |           b1
       |
       |    w1     b2
       |
       |____b0_____w2______     
       w0            
                   
                   
        answer = [ 0 , 2  , 1  ]
                   0   1   2

        Time : MN + MN log MN 
        """

        distances = []
        # Add all combinations to a heap 
        for worker_num, worker in enumerate(workers):
            for bike_num, bike in enumerate(bikes):
                distance = self.manhattan_distance(worker, bike)
                distances.append((distance, worker_num, bike_num))

        distances.sort()
        
        answers = [-1] * len(workers)
        used = set()
        
        for distance, worker, bike in distances:
            if answers[worker] == -1 and bike not in used:
                used.add(bike)
                answers[worker] = bike 
        return answers 
                                
                
                    
                
        # Pop min off heap
            # curr_distance, curr_worker, curr_bike
            # While curr_distance == heap[0]:   
                # Pop from heap and check and keep the smaller worker
                # Add the bigger worker back to the heap
                # If smaller worker == checked worker:
                    # Keep the smaller bike 
                    # Add other pair back to the heap
                
            # If the ans[curr_worker] == -1 and curr_bike isnt used: 
                # Give curr_worker the curr_bike 
                # add curr_bike to used bikes
    
    def manhattan_distance(self, points1, points2):
        return abs(points1[0] - points2[0]) + abs(points1[1] - points2[1])
    
    
    
    
    
    
    
    
s = Solution()
print(s.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))
