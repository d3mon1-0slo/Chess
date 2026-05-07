from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chess_api import api


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router, prefix="/api",tags=["api"])