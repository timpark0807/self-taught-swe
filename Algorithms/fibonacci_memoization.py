class Memo:
    
    cache = {}

    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            
        return self.fib(n-1) + self.fib(n-2)


f = Memo()
ans = f.fib(50)
print(ans)
