from django.contrib import admin
from .models import Author, Room, Message


admin.site.register(Author)
admin.site.register(Room)
admin.site.register(Message)