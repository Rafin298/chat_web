import json
import logging
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Mychats

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_1"
        print(self.room_group_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("connecting........")
        logger.info("connecting........")
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
        logger.info(data)
        message = data['msg']
        username = data['username']
        frndname = data['frndname']
        # room = data['room']

        await self.save_message(username, frndname, message)

    #     # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": 'chat_message',
                "msg": message,
                'username': username,
                'frndname': frndname
            }
        )

    # # Receive message from room group
    async def chat_message(self, event):
        message = event['msg']
        username = event['username']
        frndname = event['frndname']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'msg': message,
            'username': username,
            'frndname': frndname
        }))
        # print(event)
        # await self.send(event['msg'])

    @sync_to_async
    def save_message(self, username, frndname, message):
        user = User.objects.get(username=username)
        frndname = User.objects.get(username=frndname)

        Mychats.objects.create(me=user, frnd=frndname, content=message)