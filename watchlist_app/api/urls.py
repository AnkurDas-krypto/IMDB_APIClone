from django.contrib import admin
from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamListAV, StreamDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-details'),

    path('stream/', StreamListAV.as_view(), name = 'streamlist-list'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name = 'stream-details'),

]
