class Stock:
    def __init__(self, price, span): 
        self.price = price
        self.span = span 

class StockSpanner(object):

    def __init__(self):
        self.stack = [] 
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        currSpan = 1 
        while self.stack and price >= self.stack[-1].price:
            lastStock = self.stack.pop()
            currSpan += lastStock.span
        
        self.stack.append(Stock(price, currSpan))
        return currSpan

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
