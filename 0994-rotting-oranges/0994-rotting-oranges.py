from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        total = 0
        time = 0
        q = deque()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total += 1

                if grid[i][j] == 2:
                    q.append([i, j])
                    
        
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        while q:
            k = len(q)
            count += k 

            for _ in range(k):
                row, col = q.popleft()

                for i in range(4):
                    nrow = row + delrow[i]
                    ncol = col + delcol[i]

                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] ==1:
                        grid[nrow][ncol] = 2
                        q.append([nrow, ncol])

            if q:
                time += 1


        if total == count:
            return time

        return -1      