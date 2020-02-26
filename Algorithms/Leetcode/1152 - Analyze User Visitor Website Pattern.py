class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        
        
        username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
                      0     1     2      3       4       5       6      7       8      9 
                      
        timestamp = [1,2,3,4,5,6,7,8,9,10]
        
        
        website = ["home","about","career","home","cart","maps","home","home","about","career"]
                     0       1       2       3      4      5      6      7       8      9 
                     
        home - about - career
        home - cart - maps
        cart - maps - home
        home - about - career
        
        """
        
        processed = self.get_partition(username, timestamp, website)
        answers = collections.defaultdict(int)
        for combination in processed:
            self.backtrack(combination, answers, set(), [], 0)

        global_max = 0 
        retval = ''
        for order, count in answers.items():
            if count >= global_max:
                global_max = count
                if not retval or (retval and order < retval):
                    retval = order

        return retval.split('*')
    
    
    def backtrack(self, arr, answers, seen, curr, start):
        if len(curr) == 3:
            answers['*'.join(curr)] += 1
            return 
        
        for index in range(start, len(arr)):
            if index not in seen:
                seen.add(index)
                self.backtrack(arr, answers, seen, curr + [arr[index][1]], index+1)
                seen.remove(index)
                     
                
    def get_partition(self, username, timestamp, website):
        retval = collections.defaultdict(list)
        temp = []
        for index, name in enumerate(username):
            retval[name].append((timestamp[index], website[index]))
        
        for key, val in retval.items():
            val.sort()
    
        return list(retval.values())
                
    
    
    
    
    
    
    
    
    
    
    
    
