import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestAuthenticationAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_register_api(self):
        url = reverse('auth_register')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'john@gmail.com',
            'password': 'abcABC123!@#',
            'password2': 'abcABC123!@#'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1

    def test_register_password_not_match(self):
        url = reverse('auth_register')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'john@gmail.com',
            'password': 'abcABC123!@#',
            'password2': 'wrongpassword'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_login_api(self):
        url = reverse('auth_register')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'john@gmail.com',
            'password': 'abcABC123!@#',
            'password2': 'abcABC123!@#'
        }
        response = self.client.post(url, data)
        
        url = reverse('auth_login')
        data = {
            'username': 'johndoe',
            'password': 'abcABC123!@#'
        
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_200_OK