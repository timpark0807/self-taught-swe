class Solution(object):
    def carPooling(self, trips, capacity):
        """
        @description Returns if we take all passengers on the trip
        @param1 trips : arr[arr[int]]
        @param2 capacity : int 
        @return answer : bool         
                
                
        [num passengers, start, end]
        
                    0       1 
        trips = [[2,1,5],[3,3,7]]
                    ^  

        events : 
           
          time  event 
            1 : += 2 
            3 : += 3 
            5 : -= 2, += 3 
            7 : 
            
            curr_capacity = 2 
            
        road 
      start                           end 
        1                              7
                                      
        curr_capacity = 0 
                
        HIGHLEVEL()

        # Order the trips by start point 
        # Create events 
        # initialize passengers to 0 

        # Iterate over the events
            # perform events at that time 
            # if number of passengers > capacity:
                # return False 

        # return True 
        
        BEATIO HD
        
        Brute Force
            Best Conceivable runtime : O(n)
                -> where n == number of trips 
                -> we need to look at every trip 
            
        Edge Cases
            - Empty trips
            - 0 capacity  
            
        Assumptions
            - All valid trips? 
            - Capacity is positive?
            - Does the driver count towards capacity? 
            - Trips ordered by start point ? 
            
        Toolbox
            - sort 
            - Iteration 
            
        TestCases
        

        
        
        
        Docstrings v 
        """

        passengers = 0 
        events = self._get_events(trips)
        
        for net_change in events:
            passengers += net_change
            if passengers > capacity:
                return False
            
        return True 
            
    def _get_events(self, trips):
        """
        @param1 trips : arr[arr[int]]
        @return events : dict() 
        Events :
            time : [pick ups and drop offs at that time]
            
        # highlevel
                
        # iterate over the trips 
        
        # add the 
            
        events = []
        Iterate over trips 
            add a positive number the 1st time
            add a negative number the 2nd time 
        
        
        trips = [[2,1,5],[3,3,7]]
                    ^  
        """
        events = collections.defaultdict(int)
        
        for num_passengers, start, end in trips:
            events[start] += num_passengers
            events[end] -= num_passengers
                
        arr = [(time, net_change) for time, net_change in events.items()]
        arr.sort()
        return [net for time, net in arr]
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
