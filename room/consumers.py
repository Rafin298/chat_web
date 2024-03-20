import json

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("yooooooo.......")
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        room = data['room']
        file_data = data['file_data']
        file_name = data['file_name']

        await self.save_message(username, room, message, file_data, file_name)

    #     # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'file_data': file_data,
                'file_name':  file_name
            }
        )

    # # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        file_data = event.get('file_data', None) 
        file_name = event.get('file_name', None)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'file_data': file_data,
            'file_name':file_name
        }))

    @sync_to_async
    def save_message(self, username, room, message, file_data, file_name):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message, file_data=file_data, file_name = file_name)