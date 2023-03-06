from rest_framework import generics, permissions
from . import models, serializers

# Create your views here.
class BandsList(generics.ListCreateAPIView):
    serializer_class = serializers.BandSerializer
    queryset = models.Band.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumsList(generics.ListCreateAPIView):
    serializer_class = serializers.AlbumSerializer
    queryset = models.Album.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SongsList(generics.ListAPIView):
    serializer_class = serializers.SongSerializer
    queryset = models.Song.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewList(generics.ListAPIView):
    serializer_class = serializers.AlbumReviewSerializer
    queryset = models.AlbumReview.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewCommentList(generics.ListAPIView):
    serializer_class = serializers.AlbumReviewCommentSerializer
    queryset = models.AlbumReviewComment.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewLikeList(generics.ListAPIView):
    serializer_class = serializers.AlbumReviewLikeSerializer
    queryset = models.AlbumReviewLike.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)