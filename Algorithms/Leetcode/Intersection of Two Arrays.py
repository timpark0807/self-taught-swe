def intersection(nums1, nums2):

    """
             
    nums1 = [1, 2, 3, 4]
                      ^
             
    nums2 = [0, 3, 4, 6, 8]
                    ^

    if p1 p2 are not equal,
    increment smaller values pointer
    if equal,
     add to set, increment together
     
    """
    p1, p2 = 0, 0

    answer = set()
    
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            answer.add(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
    return list(answer)


print(intersection([1,2,3,4], [0,2,3,6]))
            
