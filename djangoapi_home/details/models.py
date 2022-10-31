from email.policy import default
from django.db import models

# Create your models here.

class Profile(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.CharField(max_length=10, default=True)
    age = models.IntegerField()
    bio = models.CharField(max_length=500)
    
    def __str__(self):
        return self.slackUsername