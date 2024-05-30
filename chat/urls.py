from django.urls import path
from .views import room , index

urlpatterns = [
    path('' , index , name='chat'),
    path('chat/<str:room_name>/' , room , name='room')
]
