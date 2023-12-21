from rest_framework.serializers import ModelSerializer
from dbuserapp.models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"
