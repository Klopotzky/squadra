from django.urls import re_path
from twisted.plugins.twisted_reactors import gi

from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer),
]