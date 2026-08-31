class Solution:
    def dfs(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 

        nrow = [-1, 0, 1, 0]
        ncol = [0, 1, 0, -1]
        grid[i][j] = 0

        for k in range(4):
            row = i + nrow[k]
            col = j + ncol[k]

            self.dfs(row, col, grid)
        
    def numEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 1:
                self.dfs(i, 0, grid)
            if grid[i][m-1] == 1:
                self.dfs(i, m-1, grid)

        for j in range(m):
            if grid[0][j] == 1:
                self.dfs(0, j, grid)
            if grid[n-1][j] == 1:
                self.dfs(n-1, j, grid)

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1

        return count