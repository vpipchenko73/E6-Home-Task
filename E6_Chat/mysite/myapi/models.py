from django.db import models
from django.contrib.auth.models import User



class Author (models.Model):
    name = models.CharField (max_length=20, unique=True )
    avatar_url = models.CharField (max_length=200, blank= True )
    avatar_name = models.CharField (max_length=20, unique=True )

    def __str__(self):
        return f'{self.avatar_name} --> {self.name}'



class Room(models.Model):
    room_name = models.CharField(max_length=20, unique=True)
    room_date = models.DateTimeField(auto_now_add=True)
    room_author = models.CharField (max_length=20, blank= True )

    def __str__(self):
        return f'{self.room_name} --> {self.room_author}'



class Message(models.Model):
    message_author = models.CharField (max_length=20)
    message_room = models.CharField (max_length=20)
    message_text = models.TextField(blank=True)
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message_author} --> {self.message_text[:15]}...'





