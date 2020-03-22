class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        
        Category
            optimization 
            
        State 
            index we are one 
            shelf_width remaining  
            
        Decisions
            place book on this shelf
            start a new shelf 
        
        Base case 
            shelf_width < 0 : return invalid
            end of all books : return valid 
        
        """
        self.memo = {} 
        self.shelf_width = shelf_width 
        return self.dp(books, shelf_width, 0, books[0][1])

    
    def dp(self, books, remain, index, max_book):
        if (remain, index, max_book) in self.memo:
            return self.memo[(remain, index, max_book)]
        
        if index == len(books):
            return max_book 
        
        continue_shelf = float('inf')
        if remain - books[index][0] >= 0:
            continue_shelf = self.dp(books, remain - books[index][0], index+1, max(max_book, books[index][1]))
            
        start_new_shelf = self.dp(books, self.shelf_width-books[index][0], index+1, books[index][1]) + max_book 
        
        self.memo[(remain, index, max_book)] = min(continue_shelf, start_new_shelf)
        return min(continue_shelf, start_new_shelf)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
