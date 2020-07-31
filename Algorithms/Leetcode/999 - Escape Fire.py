import collections 

def escapeFire(matrix):
    # https://leetcode.com/discuss/interview-question/762854/amazon-onsite-question-2020-rejected
    
    queue, fires = initStartCoord(matrix)
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    seen = set(queue[0])
    
    while queue:
        for _ in range(len(queue)):
            currRow, currCol = queue.popleft()
            if matrix[currRow][currCol] == 2:
                continue
            for move in moves:
                newRow, newCol = currRow + move[0], currCol + move[1]
                if newRow in {-1, len(matrix)} or newCol in {-1, len(matrix[0])}:
                    return True
                if matrix[newRow][newCol] == 0 and (newRow, newCol) not in seen:
                    seen.add((newRow, newCol))
                    queue.append((newRow, newCol))
                    
        _moveFire(matrix, fires)
        
    return False

def _moveFire(matrix, fires):
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    for _ in range(len(fires)):
        fireRow, fireCol = fires.popleft()
        for move in moves:
            newRow, newCol = fireRow + move[0], fireCol + move[1]
            if 0<=newRow<len(matrix) and 0<=newCol<len(matrix[0]) and matrix[newRow][newCol] != 2:
                matrix[newRow][newCol] = 2
                fires.append((newRow, newCol))

def initStartCoord(matrix):
    queue, fires = collections.deque(), collections.deque()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                queue.append((row, col))
            elif matrix[row][col] == 2:
                fires.append((row, col))
    return queue, fires

    
        

matrix = [[0,0,0,0,0,0],
          [0,2,0,0,0,0],
          [0,0,1,2,0,0],
          [0,0,2,0,0,0],
          [0,0,0,0,0,0]]
print(escapeFire(matrix))
