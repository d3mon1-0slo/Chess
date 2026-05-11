class PAWN:
    

    def check_move(self, piece, board, origin, endpoint):
        '''
            Flow:
                - check if pawn is moving sideways?
                - check if diagonal move
                - opening 2 step specially if bago yung piece
        '''
        origin_row, origin_col = origin
        target_row, target_col = endpoint

        # white moves upward
        if piece[0] == 'w':
            direction = -1
            fresh_starting = 6
        else:
            direction = 1
            fresh_starting = 1


        not_sideways = self.not_sideways(origin_col, target_col)
        diagonal_capture = self.is_diagonal(piece, origin, endpoint, board)
        one_step = self._OneStep(origin_row, target_row, direction, board, target_col)
        two_step = self.allowed_two_step(origin_row, target_row, target_col, direction, fresh_starting, board)


        # DEBUG
        # print("sideways:", not_sideways)
        # print("diagonal:", diagonal_capture)
        # print("one_step:", one_step)
        # print("two_step:", two_step)


        if diagonal_capture:
            return True

        if two_step:
            return True

        if one_step and not_sideways:
            return True

        return False
    

    # check if target is empty 
    def IsEmpty(self, board, target_row, target_col):
        return board[target_row][target_col] == ""

    def _OneStep(self, origin_row, target_row, direction, board, col):
        return target_row == origin_row + direction and board[target_row][col] == ""

    def not_sideways(self, origin_col, target_col):
        return origin_col == target_col


    # allow 2 steps on the first move 
    def allowed_two_step(self, origin_row, target_row, col, direction, fresh_starting, board):
        if origin_row != fresh_starting:
            return False

        if target_row != origin_row + (direction * 2):
            return False

        middle_row = origin_row + direction

        if board[middle_row][col] != "":
            return False

        if board[target_row][col] != "":
            return False

        return True
    

    def is_diagonal(self, piece, origin, endpoint, board):
        origin_row, origin_col = origin
        target_row, target_col = endpoint

        direction = -1 if piece[0] == 'w' else 1

        if target_row != origin_row + direction:
            return False

        if abs(target_col - origin_col) != 1:
            return False

        diagonal_target = board[target_row][target_col]

        if diagonal_target == "":
            return False 

        if diagonal_target[0] == piece[0]:
            return False 

        return True


    def move(self, piece, board, origin, endpoint):
        return self.check_move(piece, board, origin, endpoint)