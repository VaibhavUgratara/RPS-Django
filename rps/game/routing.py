from django.urls import path

from .consumers import *

websocket_urlpatterns = [
    path('ws/game/<str:roomId>', GameRoom.as_asgi() )
]