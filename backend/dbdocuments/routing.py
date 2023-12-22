from django.urls import path
from dbdocuments.consumers import MyDocumentConsumer



websocket_urlpatterns = [

    path('ws/documents/', MyDocumentConsumer.as_asgi()),
    # Add more WebSocket URL patterns if needed
]
