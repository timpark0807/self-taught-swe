def number_of_islands(matrix):
    seen = set()
    count = 0
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (row, col) not in seen:
                count += bfs(matrix, seen, row, col)
                
    return count

def bfs(matrix, seen, row, col):
    if (row, col) not in seen:

        seen.add((row, col))

        if row < 0 or row >= len(matrix):
            return
        if col < 0 or col >= len(matrix[row]):
            return

        if matrix[row][col] == 1:
            # up, down, right, left
            bfs(matrix, seen, row - 1, col)
            bfs(matrix, seen, row + 1, col)
            bfs(matrix, seen, row, col + 1)
            bfs(matrix, seen, row, col - 1)

            return 1
    return 0


matrix = [
          [1, 1, 1, 1, 0],
          [1, 1, 0, 1, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0]
          ]

print(number_of_islands(matrix))
