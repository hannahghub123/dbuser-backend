# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .api.serializers import DocumentSerializer
from  .models import Documents
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from bson import ObjectId

# @database_sync_to_async
# def get_user_documents(self, user_id):
#     user = User.objects.get(id=user_id)
#     return Documents.objects.filter(user=user)

@database_sync_to_async
def get_document_by_id(document_id):
    return Documents.objects.get(_id=document_id)

@database_sync_to_async
def delete_document_from_db(document_obj):
    document_obj.delete()

class MyDocumentConsumer(AsyncWebsocketConsumer):
    
    @database_sync_to_async
    def get_user_documents(self, user_id):
        user = User.objects.get(id=user_id)
        documents = Documents.objects.filter(user=user)
        print(documents,"###################################################################################################3")
        return documents if documents.exists() else None

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'get_documents':
            # Send initial documents to the client
            await self.get_documents(data)
        elif action == 'add_document':
            # Handle adding a new document
            await self.add_document(data)
        elif action == 'edit_document':
            # Handle editing an existing document
            await self.edit_document(data)
        elif action == 'delete_document':
            # Handle deleting a document
            await self.delete_document(data)
          

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

            await self.get_documents({ 'userId': userId })

        except Exception as e:
            print("errorrrr",e,"////////////////////")


    async def edit_document(self, data):
        pass

    @sync_to_async
    def delete_document_sync(self, documentId):
        try:
            # Filter documents based on the user ID
            document = Documents.objects.get(_id=documentId)
            userId = document.user.id
            print(userId,"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7#########################################////////")
            document.delete()

            response_data = {
                'action': 'documents_deleted',
                'message': 'document deleted successfully',
            }

            return response_data,userId

        except Exception as e:
            response_data = {
                'action': 'deleting_documents_failed',
                'message': 'An error occurred while deleting document.',
            }
            return response_data
        
    async def delete_document(self, data):
        print(data, "deleteeeeee dataaaa")

        documentId = data.get('documentId')
        try:
            object_id = ObjectId(documentId)
            print(object_id)

            # Use sync_to_async to perform database operations within the async context
            response,user = await self.delete_document_sync(object_id)

            await self.send(text_data=json.dumps(response))

            await self.get_documents({ 'userId': user })

        except Exception as e:
            print("errorrrr", e, "////////////////////")
            response_data = {
                'action': 'delete_document_failed',
                'message': 'An error occurred while deleting the document.',
            }
            await self.send(text_data=json.dumps(response_data))


    @sync_to_async
    def get_documents_sync(self, user_id):
        try:
            # Filter documents based on the user ID
            documents = Documents.objects.filter(user_id=user_id)

            # Serialize the documents
            serialized_documents = DocumentSerializer(documents, many=True).data

            response_data = {
                'action': 'documents_fetched',
                'documents': serialized_documents,
                
            }

            return response_data

        except Exception as e:
            response_data = {
                'action': 'fetch_documents_failed',
                'message': 'An error occurred while fetching documents.',
            }
            return response_data

    async def get_documents(self, data):
        try:
            # Retrieve the user ID from the data
            user_id = data.get('userId')

            # Fetch documents asynchronously using sync_to_async
            response_data = await self.get_documents_sync(user_id)

            # Send the response back to the WebSocket
            await self.send(text_data=json.dumps(response_data))

        except Exception as e:
            response_data = {
                'action': 'fetch_documents_failed',
                'message': 'An error occurred while fetching documents.',
            }
            await self.send(text_data=json.dumps(response_data))