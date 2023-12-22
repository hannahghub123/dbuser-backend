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
        serialized_data = serialize('json', [self], use_natural_primary_keys=True)
        return json.loads(serialized_data)[0]['fields']