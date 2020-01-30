class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        
        The restaurants are:

        0:
        Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
        Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5] 
        Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
        Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
        Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1]    

        1:
        Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
        Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
        Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1]  

        Step 1. Seperate VeganFriendly and Normal
        
        Step 2. For each rest in restaurant
                -> Check that it's price and its distance is less than specified
                    -> rest[price], rest[distance]
                -> If it is, store (-rating, -id) in a list 
                    -> (rest[rating], rest[id])
            
        Step 3. Return the abs(value) of the ids in order 
        
        """
        split_dict = self.get_split_dict(restaurants)
        rests = split_dict[veganFriendly]
        
        id_ = 0 
        rating = 1 
        price = 3
        distance = 4
        
        filtered = []
        
        for rest in rests: 
            if rest[price] <= maxPrice and rest[distance] <= maxDistance:
                filtered.append((-rest[rating], -rest[id_]))
                
        filtered.sort()
        
        return [abs(y) for x, y in filtered]
            
    def get_split_dict(self, arrs):
        temp = {0:[], 1:[]}
        for arr in arrs:
            temp[0].append(arr)
            if arr[2] == 1:
                temp[1].append(arr)
        return temp 
    
            
        
