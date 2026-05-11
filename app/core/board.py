from core.mechanics.move import ChessMove
import copy
import asyncio

DEFAULT_POSITIONS = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
]

chess_move = ChessMove()

class BoardManager:
    def __init__(self):
        self.current_board = copy.deepcopy(DEFAULT_POSITIONS)

    async def move(self, request):
        updated = await chess_move.move(request, self.current_board)
        self.current_board = updated
        return {"board": self.current_board, "valid" : chess_move.invalid}

    async def get_board(self):
        return {"board": copy.deepcopy(self.current_board)}
    
    async def turn(self):
        return {"Turn" : chess_move.turn}

    async def check_move(self):
        return {"is_invalid" : chess_move.invalid}

    async def reset_game(self):
        # restart yung state with piece first
        chess_move.turn = 'w'
        self.current_board = copy.deepcopy(DEFAULT_POSITIONS)
        return {"board": self.current_board}