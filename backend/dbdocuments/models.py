import json
from django.db import models
from djongo import models as djongo_models
from django.contrib.auth.models import User 
from django.core.serializers import serialize

class Documents(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}-{self.title}"
    
    def to_json(self):
        fields = {
            'user': str(self.user),
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
        return fields