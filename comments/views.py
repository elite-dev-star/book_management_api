from django.shortcuts import render

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer
from .pagination import CustomPagination


class ListCreateCommentAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveUpdateDestroyCommentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
