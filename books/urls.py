from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateBookAPIView.as_view(), name='get_post_books'),
    path('<int:pk>/', views.RetrieveUpdateDestroyBookAPIView.as_view(), name='get_delete_update_book'),
    path('<int:book_id>/comments/', views.RetrieveBookCommentsAPIView.as_view(), name='retrieve-book-comments'),
]