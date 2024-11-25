from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:genre_pk>/', views.movies_by_genre),
]