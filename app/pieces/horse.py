

class HORSE:
    

    def check_move(self, piece, board, origin, endpoint):
       
        origin_row, origin_col = origin
        target_row, target_col = endpoint
        
        valid_horse_move = self.is_LMove(piece, origin_row, origin_col, target_row, target_col, board)

        if valid_horse_move:
            return True
        
        return False

    def is_LMove(self,piece,  origin_row, origin_col, target_row, target_col, board):
        
        # making number absolute since pwedeng negative yung number
        row_diff = abs(origin_row - target_row)
        col_diff = abs(origin_col - target_col)

        # is it an L shape?
        # 2 vertical and 1 horizontal or 2 horizontal and 1 vertical
        if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
            return False
                
        target = board[target_row][target_col]

        if target == "":
            return True 

        if target[0] == piece[0]:
            return False  

        return True 


    def move(self, piece, board, origin, endpoint):
        return self.check_move(piece, board, origin, endpoint)