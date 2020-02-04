class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        
        DP or Greedy        
        
        N = Number of seats = len(row)
        C = Number of couples = N // 2
        
        Couples are in order, 
        0, 1
        2, 3
        
        Mapping =  {
                     0 : 1 
                     1 : 0 
                     2 : 3 
                     3 : 2,
                     4 : 5,
                     5 : 4
                     }
        
        row = [1, 3, 5, 2, 4, 0]
                  ^    
            
        Iterate over the rows
            - Check current person 
            - Check that current person index + 1 == to their partner
            - If not, find the partner's index and swap it with the + 1 index,
            - Increment point += 2 
        
        
        """ 
        partner = self.get_partner(row)
        seats = {person:index for index, person in enumerate(row)}
        curr_index = 0
        count = 0
        
        while curr_index < len(row)-1:
            curr_person = row[curr_index]
            curr_partner = partner[curr_person]
            in_seat = row[curr_index + 1]
            
            if in_seat != curr_partner:
                self._swap(row, seats, in_seat, curr_partner)
                count += 1 
            
            curr_index += 2 
                
        return count 
    
    def get_partner(self, row):
        N = len(row) 
        temp = {}
        for i in range(N):
            if i % 2 == 0:
                temp[i] = i + 1
            else:
                temp[i] = i - 1 

        return temp 
        
        
    def _swap(self, row, seats, p1, p2):
        pi1 = seats[p1]
        pi2 = seats[p2]
        seats[p1] = pi2
        seats[p2] = pi1
        row[pi1], row[pi2] = row[pi2], row[pi1]
        return 
            
            
            
