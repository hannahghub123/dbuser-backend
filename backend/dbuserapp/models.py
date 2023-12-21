from django.db import models
from djongo import models as djongo_models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

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
        return {
            '_id': str(self._id),
            'user': self.user.username,  # or any other field you want to include
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
    