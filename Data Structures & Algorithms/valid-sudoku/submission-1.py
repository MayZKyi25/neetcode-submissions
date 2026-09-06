class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # note: board[r][c] represents index 0x0 or [0][0] position in the board
        # rows[r]: numbers I've seen in this row
        # cols[c]: numbers I've seen in this column
        # squares: numbers I've seen in this square

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9): 
                if board[r][c] == ".":  
                    continue
                if(board[r][c] in rows[r]
                 or board[r][c] in cols[c] 
                 or board[r][c] in squares[(r//3, c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True




