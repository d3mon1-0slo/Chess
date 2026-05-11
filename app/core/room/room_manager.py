import random
import string

rooms = {}

class ROOM:

    def __init__(self):
        self.rooms = rooms

    async def create_room(self, room_id, board: dict):
        rooms[room_id] = {
            "board": board,
            "turn": "w",
            "host": None,
            "guest": None,
            "status": "waiting"
        }

    async def get_room(self, room_id):
        return rooms.get(room_id)

    async def join_room(self, room_id: str, player_data: dict):
        room = rooms.get(room_id)

        if not room:
            return {"success": False, "reason": "room_not_found"}

        if room.get("host") is None:
            room["host"] = player_data
            room["host"]["color"] = "w"
            return {
                "success": True,
                "role": "host",
                "color": "w",
                "room": room
            }

        if room.get("guest") is None:
            room["guest"] = player_data
            room["guest"]["color"] = "b"
            room["status"] = "ready"
            return {
                "success": True,
                "role": "guest",
                "color": "b",
                "room": room
            }

        # Room is full
        return {"success": False, "reason": "room_full"}

    def generate_room_id(self):
        return ''.join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=6
            )
        )