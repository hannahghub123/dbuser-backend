from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('confirm-otp/',ConfirmOTP.as_view(), name='confirm-otp'),
    path('reset-password/',Resetpassword.as_view(), name='reset-password'),
    path('set-password/',Setpassword.as_view(), name='reset-password'),

    path('get-documents/',GetDocuments.as_view(), name='getdocuments'),


    path('logout/',logout_view,name="logout"),
    # path('token/refresh/', token_refresh_view, name='token_refresh'),
]