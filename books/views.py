from django.shortcuts import render

from comments.serializers import CommentSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer
from .pagination import CustomPagination
from .filters import BookFilter


class ListCreateBookAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

    def perform_create(self, serializer):
        # Assign the user who created the book
        serializer.save(author=self.request.user)


class RetrieveUpdateDestroyBookAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class RetrieveBookCommentsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            comments = book.comments.all()  # Get all comments related to the book
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)