def moveZeros(nums):
    for num in nums:
        if num == 0:
            zero = nums.pop(nums.index(num))
            nums.append(zero) 
    return nums


print(moveZeros([0,1,0,3,12]))
