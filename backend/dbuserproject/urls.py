"""dbuserproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# import dbdocuments.routing



# # urlpatterns = [
# #     path("admin/", admin.site.urls),
# #     path("api/", include("dbuserapp.api.urls")),
# # ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('dbuserapp.api.urls')),
#     path("", include(dbdocuments.routing.websocket_urlpatterns)),
# ]

from django.contrib import admin
from django.urls import path, include
from dbdocuments.consumers import MyDocumentConsumer  # Update this line
import dbdocuments.routing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dbuserapp.api.urls')),
    path("", include(dbdocuments.routing.websocket_urlpatterns)),
]

# websocket_urlpatterns = [
#     path('ws/documents/', MyDocumentsConsumer.as_asgi()),
#     # Add more WebSocket URL patterns if needed
# ]