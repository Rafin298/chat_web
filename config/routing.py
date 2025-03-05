from room import routing
from privatewindow import routing as privatewindow_routing


websocket_urlpatterns = []

websocket_urlpatterns += routing.websocket_urlpatterns
websocket_urlpatterns += privatewindow_routing.websocket_urlpatterns
