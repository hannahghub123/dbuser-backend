from rest_framework.serializers import ModelSerializer
from dbdocuments.models import *

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"