class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_squares = defaultdict(set)

        rows = columns = len(board)
        for r in range(rows):
            for c in range(columns):
                curr = board[r][c]
                curr_row = seen_rows[r]
                curr_col = seen_cols[c]
                curr_square = seen_squares[(r//3, c//3)]

                if curr == ".":
                    continue

                if curr in curr_row or curr in curr_col or curr in curr_square:
                    return False

                curr_row.add(curr)
                curr_col.add(curr)
                curr_square.add(curr)
        
        return True
            