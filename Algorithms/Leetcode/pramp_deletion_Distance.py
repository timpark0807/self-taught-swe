
"""

  Goal: Find the minimum number of deletions to make two strings equal
    Contraints:
      - Edge Cases 
      - Brute Force
      - Input  : 2 strings
      - Output : int 
  
  High Level Groupings:
    1. Write the recursive brute force solution
    2. Introduce memoization to avoid recomputation 
    3. Write the bottom up approach to get rid of recursive overhead 
    
  
  Dynamic Programming:
    0. Type   
             min(decision1, decision2)
    
    
    1. State
              index of string 1 
              index of string 2
    
    2. Base Case
            Valid   : p1 == len(s1) or p2 == len(s2): return 0
            Invalid : 
            
    if s1[p1] == s2[p2]: p1 += 1 , p2 += 1

    3. Decision
            Deleting from String 1 
              dp(s1, s2, p1+1, p2) + 1 
            Deleting from String 2 
              dp(s1, s2, p1, p2+1) + 1
    
str1 = "", 
        ^

str2 = ""
        ^
9


LCS 
0 d o g 
f 0 0 0
r 0 0 0
o 0 1 1
g 0 1 2

len(str1) - LCS + len(str2) - LCS

Deletion Distance 
0 _ d o g 
_ 0 1 2 3 
f 1
r 2
o 3
g 4


"""


def deletion_distance(str1, str2):
  """
  Description: DP Function to find minimum number of deletions to make string equal
  
  Input: 2 Strings 
  Output: Integer representing minimum # of delete's
  """
  if not str1:
    return len(str2)
  elif not str2: 
    return len(str1)
  ans = dp(str1, str2, 0, 0, {}) 
  return ans if ans != float('inf') else len(str1) + len(str2)


def dp(s1, s2, p1, p2, memo):
  if (p1, p2) in memo:
    return memo[(p1, p2)]
  
  if p1 == len(s1) and p2 == len(s2):
    return 0 
  
  elif p1 == len(s1) or p2 == len(s2):
    return float('inf')
  
  elif s1[p1] == s2[p2]:
    memo[(p1, p2)] = dp(s1, s2, p1+1, p2+1, memo)
    return memo[(p1, p2)] 
  
  else:
    delete_one = dp(s1, s2, p1+1, p2, memo) + 1 
    delete_two = dp(s1, s2, p1, p2+1, memo) + 1 
    memo[(p1, p2)] = min(delete_one, delete_two)
    return memo[(p1, p2)] 



