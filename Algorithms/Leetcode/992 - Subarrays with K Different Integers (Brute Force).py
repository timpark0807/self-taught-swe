import collections

class Solution:
    def subarraysWithKDistinct(self, A, K):
    """
  Sliding Window
    1. Expand Window
    2. Meet Condition
    3. Process current subarray
    4. Invalidate Condition

  Edge Cases
    If K > len(A)
    If len(A) == 0
    
  Setup
    left, right = 0, 0
    answers = [[1,2], [1,2,1], [1,2,1,2], [2,1], [2,1,2], [1:2], [2,3]
    
    char_frequency = {int:int}

                 l2
         l
         0  1  2  3  4
    A = [1, 2, 1, 2, 3]
                  r 
    K = 2

    freq = {3:1,
            
    
    1. While Left
        reset dict
        right = left

        2. while len(freq <= 2)
            - if len(freq) == 2:
                answers.append(subarray)
            - if right == len(A): break
            - Add A[right] to dictionary += 1
            - right += 1

        3. Increment Left

    """
    
    left = 0
    answers = []
    
    while left < len(A):
        int_frequency = collections.defaultdict(int)
        right = left
        while len(int_frequency) <= K:
            if len(int_frequency) == K:
                answers.append(A[left:right])
            if right == len(A):
                break
            int_frequency[A[right]] += 1
            right += 1
        left += 1

    return len(answers)


"""
A = arr
K = int
left -> int
answers -> arr
left < len(A) -> int < int
int_frequency -> dictionary {int:int}
right -> int
while len(int_frequency) <= K -> int <= int
if len(int_frequency) == K: -> int == int
answers.append(A[left:right]) -> array append -> Array[int:int]
right == len(A) -> int == int
int_frequency[A[right]] += 1 -> dictionary[array[int]] += int
right+= 1 -> int + int
left += 1 int + int
return len(answers) -> int

K = 3

                    r   
A = [1, 2, 1, 3, 4]
     0  1  2  3  4
                 l

left = 0
answers = [[1,2,1,3], [2,1,3], [1,3,4]]

int_frequency = {4:1 
                
                

"""











        
