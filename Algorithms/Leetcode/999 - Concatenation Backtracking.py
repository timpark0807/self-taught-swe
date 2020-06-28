def solve(A):
    """
    Keyword: longest
        - optimization problem 
        - exhaustive search solution

    Highlevel Approach
        0. State
            - index: which word we are considering to either concatenate or skip
            - currConcat: the current concatenation string we have built 
            
        1. Base Case
            a. Success:
                - index == len(A) and currConcat is valid 
                - we've checked all words and our current concatenation string HAS NO duplicates 
            b. Failure:
                - index == len(A) 
                - we've checked all words but our current concatenation string HAS duplicates

        2. Make Decisions
            a. concatentate the current word to our current concatenation string
                - add word to currConcat
                - increment index 
            b. skip the current word
                - increment index
            
        3. Return most optimal of all decisions
    """
    return dfs(A, 0, '') 
    
    
def dfs(A, index, currConcat):
    # 1a. Success Base Case  
    if index == len(A) and isValid(currConcat):
        return len(currConcat) 
        
    # 1b. Failure Base Case 
    if index == len(A):
        return 0
    
    # 2. Make Decisions
    concatThisWord = dfs(A, index+1, currConcat+A[index]) # 2a
    skipThisWord = dfs(A, index+1, currConcat) # 2b 
    
    # 3. Return Optimal 
    return max(concatThisWord, skipThisWord) 

def isValid(curr):
    # a set will remove duplicates thus...
    # TRUE: set('abc') = {'a', 'b', 'c'}
    # FALSE: set('aaab') = {'a', 'b'}
    check = set(curr) 
    return len(check) == len(curr) 

print(solution(["eva", "jqw", "tyn", "jan"]))
