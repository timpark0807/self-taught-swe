import heapq

def top_k(nums, k):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    heap = []

    for key, value in count.items():
        heap.append((-value, key))

    heapq.heapify(heap)
    output = []
    for i in range(k):
        output.append(heapq.heappop(heap)[1])

    return output






if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    ans = top_k(nums,  k)
    print(ans)
