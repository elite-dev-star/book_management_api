from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):  # create class to serializer model
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'year', 'author')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'books')
