from django.urls import path
# Function based view ----------------------------------------
# from watchlist_app.api.views import movie_list, movie_details
#-------------------------------------------------------------
from watchlist_app.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    # Function based view--------------------------------------
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movide-details')
    #----------------------------------------------------------
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailsAV.as_view(), name='movide-details')
    
]