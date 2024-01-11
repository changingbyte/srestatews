from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('<str:room_name>/reply', views.reply, name='room_reply'),
    path("online/onlineusers/", views.users_available , name="user_list"),
    path("online/chat/", views.ChatUpdate , name="chatupdate")

]