from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from typing import List

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.rooms = {}

    async def connect(self, websocket: WebSocket, room_id: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.rooms.setdefault(room_id, []).append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        for room_id, room_connections in self.rooms.items():
            if websocket in room_connections:
                room_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, room_id: str):
        if room_id in self.rooms:
            for connection in self.rooms[room_id]:
                await connection.send_text(message)

manager = ConnectionManager()

community_server_router = APIRouter(tags="WebSocket")

@community_server_router.websocket("/ws/{client_id}/{room_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int, room_id: str):
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}", room_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", room_id)
