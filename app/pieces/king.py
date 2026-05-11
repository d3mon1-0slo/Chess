class KING:
    def check_move(self, piece, board, origin, endpoint):
        origin_row, origin_col = origin
        target_row, target_col = endpoint

        row_diff = abs(origin_row - target_row)
        col_diff = abs(origin_col - target_col)

        if row_diff > 1 or col_diff > 1:
            return False

        target = board[target_row][target_col]
        if target == "":
            return True
        if target[0] == piece[0]:
            return False
        return True

    def move(self, piece, board, origin, endpoint):
        return self.check_move(piece, board, origin, endpoint)