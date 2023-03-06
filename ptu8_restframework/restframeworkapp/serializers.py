from rest_framework import serializers
from . import models


class BandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Band
        fields = ('id', 'name',  )


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Album
        fields = ('id','name', 'band_id')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Song
        fields = ('id','name', 'duration', 'album_id')


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.AlbumReview
        fields = ('id','album_id', 'content', 'score', 'user', 'user_id')


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.AlbumReviewComment
        fields = ('id','album_review_id', 'content', 'user', 'user_id')


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.AlbumReviewLike
        fields = ('id', 'user', 'user_id')