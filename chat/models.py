from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    sender = models.ForeignKey(
        User, related_name='Sender', blank=True,  on_delete= models.CASCADE)
    reciver = models.ForeignKey(
        User, related_name='reciver', blank=True, on_delete= models.CASCADE)
    messages = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}".format(self.pk)