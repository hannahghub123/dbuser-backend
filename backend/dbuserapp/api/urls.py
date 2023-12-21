from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),

    path('add-documents/',add_document, name='add-document'),
    path('get-documents/',get_documents, name='get-documents'),
    path('delete-documents/',delete_document, name='delete-document'),


    path('logout/',logout_view,name="logout"),
    path('token/refresh/', token_refresh_view, name='token_refresh'),
]