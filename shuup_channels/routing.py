# chat/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from shuup.apps.provides import get_provide_objects

websocket_urlpatterns = []
for channels_urls in get_provide_objects("channels_urls"):
    websocket_urlpatterns.extend(channels_urls)


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    )
})
