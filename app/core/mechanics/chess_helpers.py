


from pieces.pawn import PAWN
from pieces.rook import ROOK
from pieces.horse import HORSE
from pieces.bishop import BISHOP
from pieces.queen import QUEEN
from pieces.king import KING


pawn = PAWN()
rook = ROOK()
horse = HORSE()
bishop = BISHOP()
queen = QUEEN()
king = KING()

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
        '''
            takes the converted position then sanitize it
            returns the exact position sa array 
        '''
        piece = board[coordinate[0]][coordinate[1]]

        # if piece di nag eexist
        if piece == "" or piece is None:
            return False
        return piece

    def validate_move(self,piece, board, origin, endpoint):
        ChessPiece = piece[1]
        print(f"PIECE {piece}")
        if ChessPiece == "p":
            return pawn.move(piece, board, origin, endpoint)
        elif ChessPiece == "r":
            return rook.move(piece, board, origin, endpoint)
        elif ChessPiece == "n":
            return horse.move(piece, board, origin, endpoint)
        elif ChessPiece == "b":
            return bishop.move(piece, board, origin, endpoint)
        elif ChessPiece == "q":
            return queen.move(piece, board, origin, endpoint)
        elif ChessPiece == "k":
            return king.move(piece, board, origin, endpoint)
 
    def _update_board(self, old_coordinates, new_coordinate: tuple, piece, board: list):
        
        # place piece sa new coordinate
        board[new_coordinate[0]][new_coordinate[1]] = piece
        # remove yung old position ng piece
        board[old_coordinates[0]][old_coordinates[1]] = ""
     
        # update yung board
        return board