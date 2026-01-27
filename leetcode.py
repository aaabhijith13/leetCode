
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
        return islandsYou are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

#Connect: A cell is connected to adjacent cells horizontally or vertically.
#Region: To form a region connect every 'O' cell.
#Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
#To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

#Example 1:

#Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
```
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.


## Surrounded Regions
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
```



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        w, l = len(board), len(board[0])
        visited = [[False]*l for _ in range(w)]
        print(visited)
        dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfc(row, column):
            if row < 0 or column < 0 or row >= w or column >= l or board[row][column] != "O" or visited[row][column]:
                return 
            visited[row][column] = True
            for dx, dy in dire:
                dfc(row + dx, column + dy)
        
        for i in range(w):
            if board[i][0] == "O" and not visited[i][0]:
                dfc(i, 0)
            if board[i][l-1] == "O" and not visited[i][l-1]:
                dfc(i, l-1)

        for j in range(l):
            if board[0][j] == "O" and not visited[0][j]:
                dfc(0, j)
            if board[w-1][j] == "O" and not visited[w-1][j]:
                dfc(w-1, j)

        for i in range(w):
            for j in range(l):
                if board[i][j] != "X" and not visited[i][j]:
                    board[i][j] = "X"

