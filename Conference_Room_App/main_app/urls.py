from django.urls import path
from .views import (home_page, add_new_room, rooms_list, room_name,
                    delete_room, modify_room, reserve_room, search_room)
app_name = 'main_app'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('new/', add_new_room, name='add_new_room'),
    path('list/', rooms_list, name='rooms_list'),
    path('<int:room_id>/', room_name, name='room_name'),
    path('delete/<int:room_id>/', delete_room, name='delete_room'),
    path('modify/<int:room_id>/', modify_room, name='modify_room'),
    path('reserve/<int:room_id>/', reserve_room, name='reserve_room'),
    path('search/', search_room, name='search_room'),
]
