class ROOK:
    def check_move(self, piece, board, origin, endpoint):
        '''
            - move must be vertical and horizontal only
            - if may piece sa way ng rook == endpoint 
            - if yung piece na nasa horizontal / vertical is opposite color 
                then pwede icapture
        '''
        origin_row, origin_col = origin
        target_row, target_col = endpoint

        # Check dapat vertical / horizontal move
        if origin_row != target_row and origin_col != target_col:
            return False
        
        valid_rook_move = self.get_direction(piece, origin_row, target_row, origin_col, target_col, board)

        if valid_rook_move == True:
            print("Trueee")
            return True
        print("! True")
        return False

    # check if may piece sa path if yes then cannot skip
    def get_direction(self, piece, origin_row, target_row, origin_col, target_col, board):
        row_step = 0
        col_step = 0

        # check if yung origin point is mataas (plus 1) or mababa(minus 1) kumpara sa target point
        # one at a time either ROW or COL
        if origin_row > target_row:
            row_step = - 1
        elif origin_row < target_row:
            row_step = 1

        if origin_col > target_col:
            col_step = - 1
        elif origin_col < target_col:
            col_step = 1

        # check path bawal harang
        current_row = origin_row + row_step
        current_col = origin_col + col_step
        while(current_row != target_row or current_col != target_col):
            
            # check if may piece sa harap natin or wala
            if board[current_row] [current_col] != "":
                return False
            
            # count yung paths towards target
            current_row += row_step
            current_col += col_step
        
        # locate target
        target_piece = board[target_row][target_col]

        if target_piece == "":
            return True
        
        # check if yung target is same color ng piece natin
        if target_piece[0] == piece[0]:return False

        return True

    def move(self, piece, board, origin, endpoint):
        return self.check_move(piece, board, origin, endpoint)

