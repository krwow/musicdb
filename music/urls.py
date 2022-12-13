from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # Album views.
    path('', views.album_list, name='album_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:album>/',
        views.album_detail,
        name='album_detail'),
    path('create/', views.album_create, name='create'),
    path('add_track/', views.add_track, name='track'),
]