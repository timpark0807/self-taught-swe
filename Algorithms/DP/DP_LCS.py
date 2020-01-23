class Solution(object):
    """
    Longest Common Substring and Subsequnce
    
    Similarities:
        Choices
            1. Letters match
                -> Increment count by 1, decrement both pointers by 1
            2. Letters do not match
                -> Decrement each pointer by 1, take max
                
        Evaluation Order
            1. We evaluate from the end of the string
                -> Answers to subproblem depends on smaller subproblems
                
        Base Case:
            1. If either pointer is out of bounds
                -> The longest common substring or subsequence is 0
                
    Differences:
        How we build count
            1. Subsequence
                -> Count is built inside function and added to the value of take

            2. Substring
                -> Count is built as a parameter, added to the parameter we pass in to function
                -> We need to consider the counts of functions before our current recursive call in our answer
                -> Count is part of the state 
                
        Base Case
            1. Subsequence
                -> We return 0
                -> This 0 gets returned back and +1 is added from take
            2. Substring
                -> We return count
                -> Count has been getting built inside parameters, return it. 
                
    """
    def longestCommonSubsequence(self, text1, text2):
        return self.dp_lcs_subseq(text1, text2, len(text1)-1, len(text2)-1)

    def dp_lcs_subseq(self, s1, s2, p1, p2):
        if p1 < 0 or p2 < 0:
            return 0
        take = 0
        if s1[p1] == s2[p2]:
            take = self.dp_lcs_subseq(s1, s2, p1-1, p2-1) + 1
        leave = max(self.dp_lcs_subseq(s1, s2, p1-1, p2),
                    self.dp_lcs_subseq(s1, s2, p1, p2-1))
        return max(take, leave)

    def longestCommonSubstring(self, A, B):
        return self.dp_lcs_substr(A, B, len(A)-1, len(B)-1, 0)
    
    def dp_lcs_substr(self, A, B, p1, p2, count):
        if p1 < 0 or p2 < 0:
            return count
        take = 0 
        if A[p1] == B[p2]:
            take = self.dp_lcs_substr(A, B, p1-1, p2-1, count + 1) 
        leave = max(self.dp_lcs_substr(A, B, p1, p2-1, 0), 
                    self.dp_lcs_substr(A, B, p1-1, p2, 0))
        return max(take, leave, count)
    
