from django.urls import re_path

from websocket.consumers.log import LogConsumer

websocket_urlpatterns = [
    re_path(r"ws/log$", LogConsumer.as_asgi()),
]
