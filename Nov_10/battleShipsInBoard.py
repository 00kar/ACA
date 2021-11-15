class Solution:
    def countBattleships(self, board):
        count = 0
        rows, columns = len(board), len(board[0])
        for row in range(rows):
            for col in range(columns):
                if (board[row][col] == ".") or\
                   (row > 0 and board[row - 1][col] == "X") or\
                   (col > 0 and board[row][col - 1] == "X"):
                    continue
                count += 1
        return count
    
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(Solution().countBattleships(board))
