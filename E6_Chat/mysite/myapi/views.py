from django.shortcuts import render

from rest_framework import viewsets

from .models import Author, Room, Message
from .serializers import AuthorSerializer, RoomSerializer, MessageSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('room_date')
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
   queryset = Message.objects.all().order_by('message_date')
   serializer_class = MessageSerializer


