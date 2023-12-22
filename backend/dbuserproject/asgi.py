import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import dbdocuments.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbuserproject.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        dbdocuments.routing.websocket_urlpatterns
    ),
})

