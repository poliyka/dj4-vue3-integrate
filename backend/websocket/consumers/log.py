import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer

from websocket.utils import retrieve_log_data
from typing import Any


class LogConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self) -> None:
        await self.channel_layer.group_add("log", self.channel_name)
        await self.accept()
        await self.send_json(content={"message": "connected Success !!"})

    async def disconnect(self, close_code: Any) -> None:
        await self.channel_layer.group_discard("log", self.channel_name)

    async def receive(self, text_data: str) -> None:
        parsed = json.loads(text_data)

        await self.channel_layer.group_send(
            "log",
            {
                "type": "control_message",
                **parsed,
            },
        )


    async def control_message(self, event: dict) -> None:
        await self.send_json(content=event)

