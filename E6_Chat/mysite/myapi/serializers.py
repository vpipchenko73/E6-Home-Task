# serializers.py
from rest_framework import serializers
from .models import Author, Room, Message


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

#     name = serializers.SlugRelatedField(
#         #many=True, #используется  ManyToMany
#         read_only=True,
#         slug_field='email'
#     )
    class Meta:
        model = Author
        fields = ['id', 'name', 'avatar_url', 'avatar_name']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_name', 'room_date','room_author' ]



class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'message_author', 'message_room', 'message_text', 'message_date']


