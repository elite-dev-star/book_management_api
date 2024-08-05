from django.db import models

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
