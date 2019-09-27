class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        
        Input:
        s: "cbaebabacd" p: "abc"

        Output:
        [0, 6]
        """
        answer = [] 
        begin = 0
        end = 0
        freq, count = self.get_count(p)

        while end < len(s):
            
            for i in range(len(p)):
                if s[end] in freq and freq[s[end]] > 0:
                    freq[s[end]] -= 1
                    count -= 1
                    
                end += 1

            if count == 0:
                answer.append(begin)
                
            if end >= len(s):
                return answer
            
            begin += 1
            end = begin
            freq, count = self.get_count(p)

        return answer 
        

    def get_count(self, p):
        freq = {}
        count = 0 
        for letter in p:
            count += 1
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        return freq, count 
        
s1 = "cbaebabacd"
s2 = "abc"

s= Solution()
print(s.findAnagrams(s1, s2))
