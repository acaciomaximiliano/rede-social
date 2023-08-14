from django.db import models

class chats(models.Model):
    idchat= models.AutoField(primary_key=True)
    sender = models.CharField(max_length=250)
    recipient = models.CharField(max_length=250)
    message = models.TextField()
    date_sent = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.idchat

# Create your models here.
