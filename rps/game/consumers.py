import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import GameRoomInfo
from channels.db import DatabaseSyncToAsync


class GameRoom(AsyncWebsocketConsumer):
    group_connections=dict()
    async def connect(self):
        self.RoomID=self.scope["url_route"]["kwargs"]["roomId"]
        await self.channel_layer.group_add(self.RoomID,self.channel_name)

        if self.RoomID not in GameRoom.group_connections:
            GameRoom.group_connections[self.RoomID]=[]
        
        user=str(self.scope["user"].username)
        if(user not in GameRoom.group_connections[self.RoomID]):
            GameRoom.group_connections[self.RoomID].append(user)

        if len(GameRoom.group_connections[self.RoomID]) == 2:
            await self.channel_layer.group_send(self.RoomID,{"type" : "matchStart","start" : "yes",})

        if(len(GameRoom.group_connections[self.RoomID])>2):
            GameRoom.group_connections[self.RoomID].pop()
            await self.channel_layer.group_discard(self.RoomID,self.channel_name)
            await self.close()
            return
        
        await self.accept()
        
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.RoomID,self.channel_name)
    
    async def receive(self, text_data=None, bytes_data=None):
        ROOM=await self.get_room(self.RoomID)
        info=json.loads(text_data)
        if(ROOM.player1 is None):
            ROOM.player1 = str(self.scope["user"].username)
            ROOM.choice1 = info["choice"]
            await self.save_room(ROOM)
            await self.send(text_data=json.dumps({"choice":info["choice"]}))
        else:
            ROOM.player2 = str(self.scope["user"].username)
            ROOM.choice2 = info["choice"]
            await self.save_room(ROOM)
            await self.send(text_data=json.dumps({"choice":info["choice"]}))

            user1=ROOM.player1
            user2=ROOM.player2

            choice1=ROOM.choice1
            choice2=ROOM.choice2

            if choice1 == choice2:
                result="Draw"
            elif (choice1=="Rock" and choice2=="Scissors") or\
                (choice1=="Paper" and choice2=="Rock") or\
                (choice1=="Scissors" and choice2=="Paper"):
                result=user1+" is winner!!"
            elif(choice1=="None" and choice2!="None"):
                result=user2+" is winner!!"
            elif(choice2=="None" and choice1!="None"):
                result=user1+" is winner!!"
            else:
                result=user2+" is winner!!"

            ROOM.player1=None
            ROOM.player2=None
            ROOM.choice1=None
            ROOM.choice2=None
            GameRoom.group_connections[self.RoomID]=[]
            await self.save_room(ROOM)
            await self.channel_layer.group_send(self.RoomID,{"type" : "messageHandler","result" : result,})
    
    async def messageHandler(self,event):
        gamewinner=event["result"]
        await self.send(text_data=json.dumps({"winner":gamewinner}))

    async def matchStart(self,event):
        match=event["start"]
        await self.send(text_data=json.dumps({"start":match}))

    @DatabaseSyncToAsync
    def save_room(self,obj):
        obj.save()

    @DatabaseSyncToAsync
    def get_room(self,roomId):
        try:
            return GameRoomInfo.objects.get(room_id=roomId)
        except GameRoomInfo.DoesNotExist:
            return GameRoomInfo(room_id=roomId)