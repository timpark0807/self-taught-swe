class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = [0, 0]
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start = [row, col]
                if grid[row][col] != -1:
                    count += 1
        return self.helper(grid, start[0], start[1], set(), count-1)

    def helper(self, grid, curr_row, curr_col, seen, count):
        if (curr_row, curr_col) in seen or curr_row >= len(grid) or curr_col >= len(grid[0]) or curr_row < 0 or curr_col < 0 or grid[curr_row][curr_col] == -1:
            return 0

        if grid[curr_row][curr_col] == 2 and len(seen) == count:
            return 1

        seen.add((curr_row, curr_col))
        go_right = self.helper(grid, curr_row, curr_col+1, seen, count)
        go_down = self.helper(grid, curr_row+1, curr_col, seen, count)
        go_up = self.helper(grid, curr_row-1, curr_col, seen, count)
        go_left = self.helper(grid, curr_row, curr_col-1, seen, count)
        seen.remove((curr_row, curr_col))

        return go_right + go_down + go_up + go_left 
