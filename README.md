# Chess App

A classic chess game with a FastAPI backend and a vanilla JS frontend.

---

## Project Structure

```
chess/
├── app/
│   ├── main.py                     # FastAPI app entry point
│   ├── core/
│   │   ├── board.py                # State manager — owns current_board
│   │   ├── game.py                 # Game orchestration
│   │   ├── constant.py             # Shared constants
│   │   └── mechanics/
│   │       └── move.py             # Move validation and execution
│   ├── pieces/
│   │   ├── piece.py                # Base piece class
│   │   ├── pawn.py
│   │   ├── rook.py
│   │   ├── horse.py
│   │   ├── bishop.py
│   │   ├── queen.py
│   │   └── king.py
│   ├── chess_api/
│   │   └── api.py                  # Route definitions
│   ├── models/
│   │   └── chess_model.py          # Pydantic request models
│   ├── schemas/
│   │   └── move.py                 # Move schema
│   ├── services/
│   │   └── game_service.py         # Business logic layer
│   ├── config/
│   │   └── settings.py             # App settings
│   └── frontend/
│       ├── index.html              # UI — pure visualizer, zero chess logic
│       └── static/
│           ├── index.js            # Frontend client
│           └── index.css           # Board styles
└── tests/                          # Test suite
```

---

## How It Works

The app is split into two clear responsibilities:

- **Backend** — owns all chess logic, validates moves, manages board state
- **Frontend** — pure visualizer, renders whatever the backend returns, no chess rules live here

### Board State Lifecycle

```
BoardManager.__init__()  →  current_board = deepcopy of DEFAULT_POSITIONS
move()                   →  current_board = updated board after each move
reset_game()             →  current_board = deepcopy of DEFAULT_POSITIONS
get_board()              →  returns current_board as-is (read only)
```

`DEFAULT_POSITIONS` is a constant that is never mutated. `copy.deepcopy()` is used at init and reset to create an independent copy so moves never corrupt the original default.

---

## API Endpoints

| Method | Endpoint     | Description                                       |
| ------ | ------------ | ------------------------------------------------- |
| GET    | `/api/board` | Returns the current board state                   |
| POST   | `/api/move`  | Accepts a move, returns updated board             |
| POST   | `/api/reset` | Resets the board to the default starting position |

### Move Request Body

```json
{
  "origin": "e2",
  "endpoint": "e4"
}
```

### Board Response

```json
{
  "board": [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
  ]
}
```

### Piece Codes

| Code      | Piece  |
| --------- | ------ |
| `wp` `bp` | Pawn   |
| `wr` `br` | Rook   |
| `wn` `bn` | Knight |
| `wb` `bb` | Bishop |
| `wq` `bq` | Queen  |
| `wk` `bk` | King   |

`w` = white, `b` = black. Empty squares are `""`.

---

## Setup

### Requirements

- Python 3.13+
- FastAPI 0.136+
- Uvicorn

### Installation

```bash
# Clone the repo
git clone <your-repo-url>
cd chess

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r venv/bin/requirements.txt
```

### Running the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Opening the Frontend

Open `app/frontend/index.html` directly in your browser. Make sure the backend is running first.

---

## Frontend

The frontend (`index.html` + `index.js`) is a pure visualizer — it contains zero chess logic. It communicates with the backend via three fetch calls and renders whatever the backend returns.

Two-click flow for moves:

1. First click selects a square and highlights it
2. Second click sends `POST /api/move` with the origin and destination

The **New Game** button calls `POST /api/reset` and re-renders the board from the response.

---

## Screenshots

![Chess App](https://media.discordapp.net/attachments/1325860126141186145/1502044611940716706/preview.png?ex=69fe478e&is=69fcf60e&hm=c0aff25b38d94165ede12fe5dcbb81f7cb28df4e2a74da9ad23acba27526e8c0&=&format=webp&quality=lossless&width=1206&height=1270)

---

## TODO

- [] King "Check" functionality.
- [] Chat with opponent.
