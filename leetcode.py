
#Island Problem
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        ro, col = len(grid), len(grid[0])
        def dfc(rows, columns):
            if rows < 0 or columns < 0 or rows >= ro or columns >= col or grid[rows][columns] == "0":
                return
            grid[rows][columns] = "0"
            for dx, dy in direc:
                dfc(rows + dx, columns + dy)
        for row in range(ro):
            for column in range(col):
                if grid[row][column] == "1":
                    islands += 1
                    dfc(row, column)
        return islands