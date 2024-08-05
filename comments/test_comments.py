import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from books.models import Book
from .models import Comment

User = get_user_model()

@pytest.mark.django_db
class TestCommentAPI:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.book = Book.objects.create(
            title='Test Book',
            year=2024,
            genre='Action',
            author=self.user
        )

    def test_create_comment(self):
        url = reverse('get_post_comments')
        data = {
            'content': 'Test Content',
            'book_id': self.book.id
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Comment.objects.count() == 1
        assert Comment.objects.get().content == 'Test Content'

    def test_get_comment(self):
        comment = Comment.objects.create(
            content='Test Content',
            book=self.book,
            author=self.user
        )
        url = reverse('get_delete_update_comment', kwargs={'pk': comment.id})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['content'] == comment.content

    def test_update_comment(self):
        comment = Comment.objects.create(
            content='Test Content',
            book=self.book,
            author=self.user
        )
        url = reverse('get_delete_update_comment', kwargs={'pk': comment.id})
        updated_data = {'content': 'Updated Comment', 'book_id': self.book.id}
        response = self.client.put(url, updated_data)
        assert response.status_code == status.HTTP_200_OK
        comment.refresh_from_db()
        assert comment.content == 'Updated Comment'

    def test_delete_comment(self):
        comment = Comment.objects.create(
            content='Test Comment',
            book=self.book,
            author=self.user
        )
        url = reverse('get_delete_update_comment', kwargs={'pk': comment.id})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Comment.objects.count() == 0
