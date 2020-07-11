class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        
        
        
        shortest -> looking for optimal solution 
        
        colors = [1,1,2,1,3,2,2,3,3]
                  ^
                  
                 []
        
        
        
        queries = [[1,3],[2,2],[6,1]]
                     ^  
        
        precompute the minimum distance for each color
            - Iterate through queries and return the queries 
            
        
        """
        
        left, right = self.processColors(colors)
        

        answer = []
        for index, color in queries:
            if left[index][color] == -1:
                answer.append(right[index][color])
            elif right[index][color] == -1:
                answer.append(left[index][color])
            else:
                answer.append(min(right[index][color], left[index][color]))
        return answer 
    
    def processColors(self, colors):
        left = [{i:-1 for i in range(1, 4)} for _ in range(len(colors))] 
        right = [{i:-1 for i in range(1, 4)} for _ in range(len(colors))] 
     
        for index, color in enumerate(colors):
            left[index][color] = 0 
            right[index][color] = 0 

        for index in range(1, len(colors)):
            for color in range(1, 4):
                if colors[index] != color and left[index-1][color] != -1:
                    left[index][color] = left[index-1][color] + 1
                 
        for index in reversed(range(len(colors)-1)):
            for color in range(1, 4):
                if colors[index] != color and right[index+1][color] != -1:
                    right[index][color] = right[index+1][color] + 1
        return left, right  
            
    
    
    

    
    
    
