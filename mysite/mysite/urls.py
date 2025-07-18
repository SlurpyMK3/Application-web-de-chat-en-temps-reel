from django.contrib import admin
from django.urls import include, path
from chat.views import connexion
from chat.views import inscription
from chat.views import deconnexion
from chat.views import home
from chat.views import chat

from chat.views import contact_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home, name="home"), 
    path("chat/", chat, name="chat"),
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path("connexion/", connexion, name="connexion"),  
    path("inscription/", inscription, name="inscription"),  
    path("deconnexion/", deconnexion, name="deconnexion"),

    path("contact/", contact_view, name="contact"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)