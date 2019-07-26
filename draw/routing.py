# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
   url(r'^ws/draw$', consumers.DrawConsumer),
   url(r'^ws/draw/voteSmall$', consumers.DrawConsumer),
   url(r'^ws/draw/voteLarge$', consumers.DrawConsumer),
   url(r'^ws/draw/wst$', consumers.DrawConsumer),
]

# websocket_urlpatterns = [
#    url(r'^ws/draw/voteSmall$', consumers.DrawConsumer),
# ]

