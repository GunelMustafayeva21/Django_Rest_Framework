from django.urls import path
# Function based view ----------------------------------------
# from watchlist_app.api.views import movie_list, movie_details
#-------------------------------------------------------------
from watchlist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV, ReviewList

urlpatterns = [
    # Function based view--------------------------------------
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movide-details')
    #----------------------------------------------------------
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name='stream-platform-details'),
    path('review/', ReviewList.as_view(), name='review-list'),
]