from django.urls import path, include
from watchlist_app.api.views import *
urlpatterns = [
    
    path('list/', movie_list, name='movie_list'),
    path('<int:pk>', movie_details, name='movie-details'),
]