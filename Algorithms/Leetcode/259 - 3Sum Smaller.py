class Solution:
    def threeSumSmaller(self, nums, target):
        """
        variables needed:
        answers = []
        index
        left, right
        current_triplet_sum

                       l
                    i        r
        nums = [-2, 0, 1, 3, 4]
                 0  1  2  3  4
                 
        target = 6


        0. Sort nums
        1. Iterate over nums with i
        
        while left < right
        2. Check every triplet using
            -> left = i + 1
            -> right = len(nums)-1
            
        4. If triplet < target:
            answers.append(triple)
            left += 1
            
        5. If triplet >= target:
            right -= 1

        return len(answers)
            
        """
        
        answer = 0
        nums.sort()
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_triplet = nums[i] + nums[left] + nums[right]
                if current_triplet < target:
                    answer += (right - left)
                    left += 1
                else:
                    right -= 1

        return answer
    
s = Solution()
print(s.threeSumSmaller([-2, 0, 1, 3], 2))
"""
=
nums -> arr[ints]
target -> int
answers -> arr
for i in range(int):
left = i + 1 -> int + int
right = int - int -> int
while left < right -> int < int
current_triplet = arr[int] + arr[int] + arr[int] -> int + int + int
if current_triplet < target: -> int < int
answers.append([arr[int], arr[int], arr[int]])
left += 1 -> int + int
right -= 1 -> int - int
return len(arr) -> int

answers = [[-2, -1, 6],
           [-2, 1, 4],
           
                      ]

             i 
nums = [-2, -1, 1, 4, 6]
                l
                r
target = 4

current_triplet = -1 + 1 + 4 = 4

"""



    
            
