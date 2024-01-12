from django.urls import path
from .views import home_page, add_new_room, rooms_list, room_name, delete_room
app_name = 'main_app'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('new/', add_new_room, name='add_new_room'),
    path('list/', rooms_list, name='rooms_list'),
    path('<int:room_id>/', room_name, name='room_name'),
    path('delete/<int:room_id>/', delete_room, name='delete_room'),
]
