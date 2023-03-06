from django.urls import path
from . import views

urlpatterns = [
     path('', views.BandsList.as_view()),
     path('albums/', views.AlbumsList.as_view()),
     path('songs/', views.SongsList.as_view()),
     path('albums/reviews/', views.AlbumReviewList.as_view()),
     path('albums/reviews/comments/', views.AlbumReviewCommentList.as_view()),
     path('albums/reviews/likes/', views.AlbumReviewLikeList.as_view()),
]
