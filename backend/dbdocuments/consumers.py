# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .api.serializers import DocumentSerializer
from  .models import Documents
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

class MyDocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'get_documents':
            # Send initial documents to the client
            await self.send_documents(data['userId'])
        elif action == 'add_document':
            # Handle adding a new document
            await self.add_document(data)
        elif action == 'edit_document':
            # Handle editing an existing document
            await self.edit_document(data)
        elif action == 'delete_document':
            # Handle deleting a document
            await self.delete_document(data)

    async def send_documents(self, userId):
        pass


    async def add_document(self, data):
        print(data, "dataaaaa///////////////////////")
        action = data.get('action')

        document_data = data.get('documentData', {})
        print(document_data, "dataaaaa///////////////////////in add")

        title = document_data.get('title')
        content = document_data.get('content')

        try:
            userId = data["documentData"]["userId"]
            user_obj = await sync_to_async(User.objects.get)(id=userId)
            documentsobj = await sync_to_async(Documents.objects.create)(user=user_obj, title=title, content=content)
            serialized = DocumentSerializer(documentsobj)
            response_data = {
                'action': 'document_added',
                'message': 'Document added successfully',
                'documents' : serialized.data
            }
            await self.send(text_data=json.dumps(response_data))

            # await self.send_documents(userId)

        except Exception as e:
            print("errorrrr",e,"////////////////////")


    async def edit_document(self, data):
        # Logic to edit an existing document in the database
        # ...
        pass

    async def delete_document(self, data):
        # Logic to delete a document from the database
        # ...
        pass
