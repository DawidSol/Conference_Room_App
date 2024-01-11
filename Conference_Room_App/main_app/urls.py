from django.urls import path
from .views import home_page, add_new_room
app_name = 'main_app'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('new/', add_new_room, name='add_new_room'),
]
