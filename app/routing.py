# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter , get_default_application
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()



import chat.routing
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})