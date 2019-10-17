import heapq

def top_k(nums, k):
    """
    Given a non-empty array of integers,
    return the k most frequent elements.
    """
    if nums == []:
        return []
    
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    temp = []
    for key, value in count.items():
        temp.append((-value,key))

    heapq.heapify(temp)

    answer = []

    for i in range(k):
        answer.append(heapq.heappop(temp)[1])


    return answer 
    

nums = [1,1,1,2,2,3, 6,6 ,6,6, 7,7 ,7,7,7]
k = 2
ans = print(top_k(nums,k))
