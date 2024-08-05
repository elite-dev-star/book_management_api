from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateCommentAPIView.as_view(), name='get_post_comments'),
    path('<int:pk>/', views.RetrieveUpdateDestroyCommentAPIView.as_view(), name='get_delete_update_comment'),
]