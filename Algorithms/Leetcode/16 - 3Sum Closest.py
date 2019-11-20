class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        
        nums = [-1, 2, 1, -4]
        
        
        nums = [-4, -1, 1, 2]
                     i  l     
                        r   
        
        answer = 2
        global_distance = 1
        current_sum = -1 + 1 + 2 = 2
        need = 4
        current_distance = 1 - 2 = 1
        
        -3 -2 -1 0 1
                           
                           
        variables needed:
        global_min 
        answer
        left, right 
        nums.sort()
        
        
        1. Iterate over nums with i
            -> left = i + 1
            -> right = len(nums) - 1
            -> need = -nums[i]
        2. while left < right:
            # Log and proccess current triplet
                current_sum = nums[i] + nums[left] + nums[right] 
                current_distance = abs(target - (current_sum))
                if current_distance < global_distance:
                    global_distance = current_distance
                    answer = current_sum
            # move left and right 
            if nums[left] + nums[right] > need:
                right -= 1
            else:
                left += 1

        """              
        global_distance = float('inf')
        answer = 0
        nums.sort()
        if len(nums) < 3:
            return []
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            need = -nums[i]
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_distance = abs(target - current_sum)
                if current_distance < global_distance:
                    global_distance = current_distance
                    answer = current_sum
                    
                if current_sum > target:
                    right -= 1
                else:
                    left += 1        
        
        return answer

"""

target = 1

         0   1  2  3
nums = [-3,  0, 1, 2]
         i   l
                   r
                      
global_distance = 2
answer = -1

      c 
i -> (0, 1)

nums[left] = 0
nums[right] = 2 

current_sum = -3 + 0 + 2 = -1
current_distance = 1 - -1 = 2


"""























    
