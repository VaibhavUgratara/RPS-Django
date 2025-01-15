from django.db import models
import django, os

# Create your models here.
class GameRoomInfo(models.Model):
    room_id=models.CharField(primary_key=True,max_length=20)
    player1=models.CharField(max_length=150, null=True)
    player2=models.CharField(max_length=150, null=True)
    choice1=models.CharField(max_length=10, null=True)
    choice2=models.CharField(max_length=10, null=True)
    