from fastapi import APIRouter, WebSocket, WebSocketDisconnect,HTTPException
from collections import defaultdict

from core.board import BoardManager
from models.chess_model import MoveRequest
from core.mechanics.move import ChessMove
from core.room.room_manager import ROOM

router = APIRouter()

room_manager = ROOM()
rooms = room_manager.rooms

board = BoardManager()
chess = ChessMove()

connections = defaultdict(set)


@router.get("/user_turn")
async def get_user_turn():
    return await board.turn()


@router.get("/check_move")
async def check_user_move():
    return await board.check_move()


@router.get("/board/{room_id}")
async def get_board(room_id: str):
    room_data = rooms.get(room_id)

    if not room_data:
        raise HTTPException(status_code=404, detail="Room not found")

    return {
        "board": room_data["board"],
        "turn": room_data["turn"]
    }


@router.post("/reset")
async def reset_board():
    return await board.reset_game()


@router.post("/create_room")
async def create_room():
    room_id = room_manager.generate_room_id()
    
    initial_board = await board.reset_game()
    board_data = initial_board.get("board") if isinstance(initial_board, dict) else initial_board

    await room_manager.create_room(room_id, board_data)
    return {
        "room_id": room_id,
        "link": f"http://127.0.0.1:5500/?room={room_id}"
    }


@router.get("/get_room")
async def get_room():
    return await room_manager.get_room("SJSDND")


@router.post("/join-room/{room_id}")
async def join_room(room_id: str, payload: dict):

    result = await room_manager.join_room(room_id, payload)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["reason"])

    if result["role"] == "guest":
        await broadcast(room_id, {
            "type": "player_joined",
            "player": {
                "name": payload.get("name", "Guest"),
                "avatar": payload.get("avatar", "♙"),
                "color": result["color"]
            }
        })

    return {
        "success": True,
        "room_id": room_id,
        "role": result["role"],
        "color": result["color"],
        "room": result["room"]
    }


@router.post("/move/{room_id}")
async def move_piece(room_id: str, request: MoveRequest):

    room_data = rooms.get(room_id)

    if not room_data:
        return {"success": False, "reason": "room_not_found"}

    board_state = room_data["board"]
    turn = room_data["turn"]

    board_state, new_turn, ok, winner = await chess.move(
            request,
            board_state,
            turn
        )

    if not ok:
        return {
                "success": False,
                "board": board_state,
                "turn": turn
        }

    room_data["board"] = board_state
    room_data["turn"] = new_turn

    if winner:
        await broadcast(room_id, {
                "type": "game_over",
                "winner": winner,
                "board": board_state
        })
        return {
                "success": True,
                "board": board_state,
                "turn": new_turn,
                "winner": winner
        }

    await broadcast(room_id, {
            "type": "move",
            "board": board_state,
            "turn": new_turn
        })

    return {
            "success": True,
            "board": board_state,
            "turn": new_turn
        }


@router.websocket("/ws/{room_id}")
async def websocket_room(websocket: WebSocket, room_id: str):

    await websocket.accept()
    connections[room_id].add(websocket)

    try:
        while True:
            await websocket.receive_json()

    except WebSocketDisconnect:
        connections[room_id].remove(websocket)


async def broadcast(room_id: str, message: dict):

    if room_id not in connections:
        return

    for ws in list(connections[room_id]):
        try:
            await ws.send_json(message)
        except:
            connections[room_id].remove(ws)