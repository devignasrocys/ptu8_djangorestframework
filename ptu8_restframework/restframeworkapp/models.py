from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=150)


class Album(models.Model):
    name = models.CharField(max_length=150)
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE, related_name="albums")


class Song(models.Model):
    name = models.CharField(max_length=150)
    duration = models.IntegerField()
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="albums_reviews")
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="albums_reviews")
    content = models.CharField(max_length=1500)
    score = models.IntegerField()


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="album_review_comments")
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name="album_review_comments")
    content = models.CharField(max_length=1500)


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="album_reivew_likes")
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name="alum_review_likes")