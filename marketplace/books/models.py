from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title
