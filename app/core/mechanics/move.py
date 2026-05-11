from .chess_helpers import ChessHelpers



class ChessMove:
    '''
        - Return board status / postions
        - restart board to default pos
        - accept piece moves
    '''
    def __init__(self):
        self.chess_helpers = ChessHelpers()
        self.turn = "w"
        self.invalid = False

    # Entry point
    async def move(self, coordinates, board):
        '''
            - Convert STR to INT
            - check if position exist
            - if true then move the piece 
            - if not == invalid ./.
        '''

        origin = coordinates.origin
        endpoint = coordinates.endpoint

        convert_origin = self.chess_helpers.str_to_index(origin)
        convert_endpoint = self.chess_helpers.str_to_index(endpoint)

        # origin and endpoint becomes tuple
        # validate
        print(self.turn)
        _isValid_piece = self.chess_helpers.check_piece(convert_origin, board)
        if not _isValid_piece:
            return board
        else:
            if _isValid_piece[0] == self.turn:
                # valid_new_position = self.chess_helpers.check_destination(_isValid_piece, convert_endpoint, board)
                valid_piece_move = self.chess_helpers.validate_move(_isValid_piece, board, convert_origin, convert_endpoint)


                print(self.invalid)
                if valid_piece_move == True:
                    if self.turn == 'w':
                        self.turn = 'b'
                    else:
                        self.turn = "w"
                    
                    updated_board = self.chess_helpers._update_board(convert_origin,convert_endpoint, _isValid_piece, board)
                    self.invalid = True
                    return updated_board
                else:
                    # invalid move
                    self.invalid = False

            return board
