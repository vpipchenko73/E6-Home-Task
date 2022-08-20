import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        date = text_data_json['date']
        url_avatar = text_data_json['url_avatar']
        nic_avatar = text_data_json['nic_avatar']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'date': date,
                'url_avatar': url_avatar,
                'nic_avatar': nic_avatar
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        date = event['date']
        url_avatar = event['url_avatar']
        nic_avatar = event['nic_avatar']


        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'date': date,
            'url_avatar': url_avatar,
            'nic_avatar': nic_avatar

        }))