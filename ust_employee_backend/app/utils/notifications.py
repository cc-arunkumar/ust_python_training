import asyncio
import json
from typing import Set
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect


class NotificationManager:
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except KeyError:
            pass

    async def broadcast(self, message: dict):
        text = json.dumps(message)
        to_remove = []
        for conn in list(self.active_connections):
            try:
                await conn.send_text(text)
            except Exception:
                to_remove.append(conn)

        for conn in to_remove:
            self.disconnect(conn)


_manager = NotificationManager()


def notify_task_created(payload: dict):
    """Schedule an async broadcast notifying connected clients that a task
    was created. This is a fire-and-forget helper so it can be invoked from
    synchronous request handlers.
    """
    asyncio.create_task(_manager.broadcast(payload))


def get_manager():
    return _manager
