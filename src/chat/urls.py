from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name=  'index'),
    path('chat/<room_name>/', views.room, name=  'room'),
    path('ctest/', views.test, name=  'chat'),
]
