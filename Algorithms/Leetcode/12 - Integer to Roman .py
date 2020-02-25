class Solution:
    def intToRoman(self, num):
        if not num:
            return ''
        
        translations = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400,'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
                        (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        ans = ''
        
        while num:
            for integer, roman in translations:
                if integer <= num: 
                    ans += roman
                    num -= integer
                    break
        
        return ans 
