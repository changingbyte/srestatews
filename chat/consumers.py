from datetime import datetime
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(f"{self.room_name}_{self.room_group_name}")
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    

    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        sent = False
        message_type = text_data_json['message_type']
        if text_data_json['sent'] == "True":
            sent = True
        

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                "sender":sender,
                "sent":sent,
                "message_type":message_type,
                "timestamp":int(datetime.now().timestamp())
            }
        )

    @staticmethod
    async def send_job_notification(message, room_name):
        channel_layer = get_channel_layer()
        group_name = room_name
        await channel_layer.group_send(
        group_name,
        json.dumps({
            "type": "send.notification", 
            "message": message, 
        })
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        sent = event['sent']
        message_type = event['message_type']
        if event['sent'] == "True":
            sent = True

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender' : sender,
            "sent":sent,
            "message_type":message_type,
            "timestamp":int(datetime.now().timestamp())
        }))
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )