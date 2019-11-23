def four_sum(nums, target):
    answers = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, len(nums)):
            
            left = j + 1
            right = len(nums) - 1
            
            while left < right:
                need = target - nums[i] - nums[j]
                if nums[left] + nums[right] == need:
                    answers.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] < need:
                    left += 1
                    
                else:
                    right -= 1

    return answers
                

nums = [1,0,-1,0,-2,2]
target = 1
print(four_sum(nums, target))
