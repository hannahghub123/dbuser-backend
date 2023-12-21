# your_app/consumers.py

import json
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class MyDocumentsConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("websocket connected///////////",event)
        # await self.accept()
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("websocket received///////////", event)
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))
        print("Message is ",event['text'])

    async def websocket_disconnect(self, event):
        print("websocket disconnected///////////", event)
        # raise StopConsumer()
