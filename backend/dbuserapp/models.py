from django.db import models

class OTP(models.Model):
    otp=models.PositiveIntegerField(blank=True,null=True)
    email=models.CharField(max_length=200,blank=True,null=True)
    

    def __str__(self):
        return f"{self.otp}"