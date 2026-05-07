class ChessMove:
    '''
        - Return board status / postions
        - restart board to default pos
        - accept piece moves
    '''
    def __init__(self):
        self.chess_helpers = ChessHelpers()

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
        _isValid = self.chess_helpers.check_piece(convert_origin, board)
        print(_isValid)
        if _isValid:
            updated_board = self.chess_helpers._update_board(convert_endpoint, _isValid, board)
            return updated_board

        return board


class ChessHelpers:
    # convert yung String input into coordinates

    def str_to_index(self, pos: str):
        '''
            - takes String as input / chess move: e2
            - split the input so pos[0] = e, pos[1] = 2
            - Convert the letter E into unicode using ord() function 
            - sa Unicode letter A == 97 so gagawin natin minus lang natin yung 
            - E sa A. ord('e') - ord('a') 

            - for 2nd character naman ifo-force lang natin na maging interger yung string 
            - since integer naman talaga siya to begin with 
            - so int(pos[1])
        '''
        column = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        return row, column

    def check_piece(self, coordinate: tuple, board: list) -> list:
        print(coordinate)
        '''
            takes the converted position then sanitize it
            returns the exact position sa array 
        '''
        piece = board[coordinate[0]][coordinate[1]]

        # if piece di nag eexist
        if piece == "" or piece is None:
            return False
        else:
            # remove yung old position ng piece
            board[coordinate[0]][coordinate[1]] = ""
            return piece

    def _update_board(self, new_coordinate: tuple, piece, board: list):
        # place piece sa new coordinate
        board[new_coordinate[0]][new_coordinate[1]] = piece

        # update yung board
        return board