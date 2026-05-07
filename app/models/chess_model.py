from pydantic import BaseModel



class MoveRequest(BaseModel):
    origin: str
    endpoint:str