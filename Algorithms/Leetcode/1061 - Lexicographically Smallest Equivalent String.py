class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        """
        :type A: str
        :type B: str
        :type S: str
        :rtype: str
        """
        self.parents = [-1] * 26
        self.letterToIndex = collections.defaultdict(int)  
        self.indexToLetter = collections.defaultdict(str)  

        for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            self.letterToIndex[letter] = index
            self.indexToLetter[index] = letter 
            
        for index in range(len(A)):
            self.union(A[index], B[index])
            print(self.parents)
        ans = []
        for letter in S:
            l = self.indexToLetter[self.find(letter)]
            ans.append(l)

        return ''.join(ans) 
    
    
    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b) 
        
        if parentA == parentB:
            return
        elif parentA < parentB:
            self.parents[parentB] = parentA
        else:
            self.parents[parentA] = parentB 
            
    def find(self, letter):
        if self.parents[self.letterToIndex[letter]] == -1:
            return self.letterToIndex[letter]
        return self.find(self.indexToLetter[self.parents[self.letterToIndex[letter]]])
            
    
