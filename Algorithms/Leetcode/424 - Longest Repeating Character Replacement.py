class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        Sliding window
        Variables
        left, right = 0, 0
        freq = {'char' -> str : 0 -> int}
        global_max = 5
        max_count = 4

        freq = {'A':1, 'B':4
            
        
             0 1 2 3 4 5 6 
        s = "A A B A B B B"
                           r
                 l
             
        k = 1

        1. Expand Right
            - Add s[right] to freq
            - max_count = max(max_count, freq[s[right]])
            - right += 1
            
        2. Meet Condition
            -> There are k characters that are not the most freq character
            -> if right - left - max_count <= K:
            
            3. Process current subarray
                -> global_max = max(global_max, right-left)
                
            4. Contract window
               if right - left - max_count > K:
                -> freq[s[left]] -= 1
                -> if freq[s[left]] == 0:
                    del freq[s[left]]
                max_count = max(list(freq.values())
                left += 1

        return global_max
        
        """
        if len(s) == 0:
            return 0
        if k > len(s):
            return len(s)
        
        left, right = 0, 0
        freq = collections.defaultdict(int)
        global_max = float('-inf')
        max_count = 0

        while right < len(s):
            right_char = s[right]
            freq[right_char] += 1
            max_count = max(max_count, freq[right_char])
            right += 1

            while right - left - max_count > K:
                left_char = s[left]
                freq[left_char] -= 1
                max_count = max(list(freq.values()))
                left += 1

            global_max = max(global_max, right-left)

        return global_max

"""
s = string
K = int
left -> int
right -> int
freq -> dict[str] = int
global_max -> int
max_count -> int

while right < len(s) -> int < int
right_char = s[right] -> string[int] -> str
freq[right_char] += 1 -> freq[str] +=  int
max_count = max(int, int) -> int
right += 1 -> int + int

while right -left -max_count > K -> int - int - int > int
left_char = s[left] -> string[int] -> str
max_count = max(list(freq.values()) freq.values -> list(int)
left += 1 -> int += int
global_max = max(int, int-int) -> int
return global_max -> int

"""




    
                
