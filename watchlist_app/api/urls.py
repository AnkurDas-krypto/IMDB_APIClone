from django.contrib import admin
from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamListAV, StreamDetailAV, ReviewList,ReviewDetail,ReviewCreate

urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-details'),

    path('stream/', StreamListAV.as_view(), name = 'streamlist-list'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'stream-details'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name = 'review-details'),

    # path('review/', ReviewList.as_view(), name ="reviews"),
    # path('review/<int:pk>', ReviewDetail.as_view(), name ="review-details"),

]
