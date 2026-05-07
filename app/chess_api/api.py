from fastapi import APIRouter, HTTPException
from core.board import BoardManager
from models.chess_model import MoveRequest

router = APIRouter()
board = BoardManager()

@router.get('/board')
async def get_board():
    return await board.get_board()

@router.post('/move')
async def move_piece(request: MoveRequest):
    return await board.move(request)

@router.post('/reset')
async def reset_board():
    return await board.reset_game()