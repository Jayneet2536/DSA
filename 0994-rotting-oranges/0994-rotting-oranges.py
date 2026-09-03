class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()    
        total = 0    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] != 0:
                    total += 1

        nrow = [-1, 0, 1, 0]
        ncol = [0, 1, 0, -1]
        count = 0
        time = 0


        while q:
            
            k = len(q)

            count += k

            for _ in range(k):
                i, j = q.popleft()
                for p in range(4):
                    row = i + nrow[p]
                    col = j + ncol[p]

                    if row >= 0 and row < n and col >= 0 and col < m and grid[row][col] == 1:
                        q.append([row, col])
                        grid[row][col] = 2
                

            if q:
                time += 1

        if count == total:
            return time

        return -1