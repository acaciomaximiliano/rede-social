from django.conf import settings
from django.db import models
from django.utils import timezone


class chats(models.Model):
    idchat= models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    sender = models.CharField(max_length=250)
    recipient = models.CharField(max_length=250)
    message = models.TextField()
    date_sent = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.idchat

# Create your models here.
