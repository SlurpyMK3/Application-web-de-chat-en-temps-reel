from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path("<str:room_name>/", views.room, name="room"),
    path("connexion/", views.connexion, name="connexion"),
    path("inscription/", views.inscription, name="inscription"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),

    path("contact/", views.contact_view, name="contact"),  

]