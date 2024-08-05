import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from .models import Book

User = get_user_model()

@pytest.mark.django_db
class TestBookAPI:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_book(self):
        url = reverse('get_books')
        data = {
            'title': 'Test Book',
            'genre': 'Action',
            'year': 2024,
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.count() == 1
        assert Book.objects.get().title == 'Test Book'

    def test_get_book(self):
        book = Book.objects.create(
            title='Test Book',
            year=2024,
            genre='Action',
            author=self.user
        )
        url = reverse('get_delete_update_book', kwargs={'pk': book.id})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == book.title

    def test_update_book(self):
        book = Book.objects.create(
            title='Test Book',
            year=2024,
            genre='Action',
            author=self.user
        )
        url = reverse('get_delete_update_book', kwargs={'pk': book.id})
        updated_data = {'title': 'Updated Book', 'year': 2024, 'genre': 'Action'}
        response = self.client.put(url, updated_data)
        assert response.status_code == status.HTTP_200_OK
        book.refresh_from_db()
        assert book.title == 'Updated Book'

    def test_delete_book(self):
        book = Book.objects.create(
            title='Test Book',
            year=2024,
            genre='Action',
            author=self.user
        )
        url = reverse('get_delete_update_book', kwargs={'pk': book.id})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Book.objects.count() == 0

    def test_get_book_comments(self):
        book = Book.objects.create(
            title='Test Book',
            year=2024,
            genre='Action',
            author=self.user
        )
        book.comments.create(content='Great book!', author=self.user)

        url = reverse('retrieve-book-comments', kwargs={'book_id': book.id})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_get_book_not_found(self):
        url = reverse('get_delete_update_book', kwargs={'pk': 1000})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
