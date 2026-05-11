class BISHOP:
    def check_move(self, piece, board, origin, endpoint):
        origin_row, origin_col = origin
        target_row, target_col = endpoint

        # bishop can only move diagonal
        if abs(origin_row - target_row) != abs(origin_col - target_col):
            return False
        return self.check_path(piece, origin_row, origin_col, target_row, target_col, board)


    def check_path(self, piece, origin_row, origin_col, target_row, target_col, board):
        # determine diagonal direction
        row_step = -1 if origin_row > target_row else 1
        col_step = -1 if origin_col > target_col else 1

        # walk the path
        current_row = origin_row + row_step
        current_col = origin_col + col_step

        while current_row != target_row or current_col != target_col:
            if board[current_row][current_col] != "":
                return False
            current_row += row_step
            current_col += col_step

        # check destination
        target = board[target_row][target_col]
        if target == "":
            return True
        if target[0] == piece[0]:
            return False
        return True


    def move(self, piece, board, origin, endpoint):
        return self.check_move(piece, board, origin, endpoint)

