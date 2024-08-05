from books.models import Book
from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):  # create class to serializer model
    author = serializers.ReadOnlyField(source='author.username')
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book'
    )

    class Meta:
        model = Comment
        fields = ('id', 'content', 'book_id', 'author')
