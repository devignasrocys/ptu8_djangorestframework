from django.urls import path
from . import views

urlpatterns = [
     path('', views.BandsList.as_view()),
     path('albums/', views.AlbumsList.as_view()),
     path('songs/', views.SongsList.as_view()),
     path('albums_reviews/', views.AlbumReviewList.as_view()),
     path('albums_reviews_comments/', views.AlbumReviewCommentList.as_view()),
     path('albums_reviews_likes/', views.AlbumReviewLikeList.as_view()),
]
