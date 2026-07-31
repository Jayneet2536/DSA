class Solution:
    def func(self, board, row, ans):
        if row == len(board):
            ans.append(["".join(r) for r in board])
            return
            
        for col in range(len(board[0])):
            if self.is_available(board, row, col):
                board[row][col] = 'Q'
                self.func(board, row+1, ans)
                board[row][col] = '.'

    def is_available(self, board, row, col):
        r, c = row, col 
        while r >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
        
        r, c = row, col
        while c >=0 and r >=0:
            if board[r][c] == 'Q':
                return False
                
            c -= 1
            r -= 1

        r, c = row, col
        while r >= 0 and c < len(board):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.func(board, 0, ans)

        return ans