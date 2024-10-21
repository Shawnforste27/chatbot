import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(
            text_data=json.dumps({"text": "Hi there! How can I help you today?"})
        )

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("text", "")

        # Simple logic to respond (could be replaced by more complex logic)
        if "help" in message.lower():
            response = "Sure! I'm here to help."
        else:
            response = f"You said: {message}"

        await self.send(text_data=json.dumps({"text": response}))



