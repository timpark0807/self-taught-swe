def solution(A):
    avg = [float('inf') for _ in range(len(A))]
    start = [-1 for _ in range(len(A))]

    for index in range(1, len(A)):

        curr = (A[index-1] + A[index]) / 2
        
        goBack = (avg[index-1] * (index - start[index-1]) + A[index]) / (index - start[index-1] + 1)
        avg[index] = min(curr, goBack)
        if avg[index] == curr:
            start[index] = index-1
        else:
            start[index] = start[index-1]
    
    minAnswer = min(avg)
    for index, num in enumerate(avg):
        if num == minAnswer:
            return start[index]
            
