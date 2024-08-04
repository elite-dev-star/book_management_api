from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
