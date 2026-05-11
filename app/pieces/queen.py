class QUEEN:
    def __init__(self):
        from .rook import ROOK
        from .bishop import BISHOP
        self.rook = ROOK()
        self.bishop = BISHOP()

    def check_move(self, piece, board, origin, endpoint):
        origin_row, origin_col = origin
        target_row, target_col = endpoint

        row_diff = abs(origin_row - target_row)
        col_diff = abs(origin_col - target_col)

        if row_diff == col_diff:
            return self.bishop.check_move(piece, board, origin, endpoint)

        if origin_row == target_row or origin_col == target_col:
            return self.rook.check_move(piece, board, origin, endpoint)

        return False

    def move(self, piece, board, origin, endpoint):
        return self.check_move(piece, board, origin, endpoint)