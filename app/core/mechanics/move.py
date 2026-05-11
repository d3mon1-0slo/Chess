from .chess_helpers import ChessHelpers


class ChessMove:
    '''
        - Return board status / postions
        - restart board to default pos
        - accept piece moves
    '''
    def __init__(self):
        self.chess_helpers = ChessHelpers()

    # Entry point
    async def move(self, coordinates, board, turn):
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

        piece = self.chess_helpers.check_piece(convert_origin, board)

        if not piece:
            return board, turn, False, None

        if piece[0] != turn:
            return board, turn, False, None

        valid_piece_move = self.chess_helpers.validate_move(
            piece,
            board,
            convert_origin,
            convert_endpoint
        )

        if valid_piece_move == True:

            updated_board = self.chess_helpers._update_board(
                convert_origin,
                convert_endpoint,
                piece,
                board
            )

            new_turn = "b" if turn == "w" else "w"

            # Check if a king was captured
            winner = self.check_king_captured(updated_board)

            return updated_board, new_turn, True, winner

        # invalid move
        return board, turn, False, None

    def check_king_captured(self, board_state):
        board = board_state["board"] if isinstance(board_state, dict) else board_state

        white_king = False
        black_king = False

        for row in board:
            for cell in row:
                if cell == "wk": white_king = True
                if cell == "bk": black_king = True

        if not white_king: return "b"  # black wins
        if not black_king: return "w"  # white wins
        return None