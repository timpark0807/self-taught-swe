"""Given a string, find the length of the longest substring without repeating characters.



Example 1:


        freq = {p : 0,
                w : 1,
                k : 1,
                e : 1,
                l : 1
                

        0 1 2 3 4 5 6 7
Input: "p w w k e w l"
       0 1 2 3 4 5 6 7
              l 
                      r

        overall_max = 3
        curr_substring = 'wke'

"""
import collections


def window(string):
    if len(string) == 0:
        return 0
    
    left, right = 0, 0
    overall_max = float('-inf')
    freq = collections.defaultdict(int)

    while right < len(string):
        right_char = string[right]
        freq[right_char] += 1
        while freq[right_char] > 1:
            curr_substring = string[left:right]
            overall_max = max(overall_max, len(curr_substring))
            left_char = string[left]
            freq[left_char] -= 1
            left += 1
        right += 1

    overall_max = max(overall_max, len(string[left:right]))

    return overall_max

    

print(window('pwwkewl'))
print(window('pwwkewk'))
