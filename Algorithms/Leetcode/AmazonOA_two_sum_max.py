"""
https://leetcode.com/discuss/interview-question/356960

Find pair with given sum.

A two sum problem with a find max twist.
.
"""

nums = [20, 50, 40, 25, 30, 10]
#        0   1   2   3   4   5

target = 90

def two_sum_mod(nums, target):
    nums_dict = {}

    # add values to dict
    for index, num in enumerate(nums):
        nums_dict[num] = index

    curr_max = 0 
    # check if values exist
    for index, num in enumerate(nums):
        needed = (target - 30) - num
        if needed in nums_dict:
            # we have a pair where sums equal target - 30

            # take max of current pair 
            max_num = max(needed, num)

            # if max of current pair is greater than the current max
            if max_num > curr_max:

                # current max is now the max of our current pair
                curr_max = max_num

                # save the two indexes
                first = index
                second = nums_dict[needed]

    return [first, second]


print(two_sum_mod(nums,target))
