from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Book
from django.urls import reverse


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            description='Test Description',
            genre='Test Genre',
            year=2022,
            owner=self.user
        )
        self.book.authors.add(self.author) 

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.description, 'Test Description')
        self.assertEqual(self.book.genre, 'Test Genre')
        self.assertEqual(self.book.year, 2022)
        self.assertTrue(self.book.authors.exists()) 
        self.assertEqual(self.book.owner, self.user)
        self.assertEqual(self.book.status, 'pending')


class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.client.force_login(self.user)
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            description='Test Description',
            genre='Test Genre',
            year=2022,
            owner=self.user
        )
        self.book.authors.add(self.author) 
        
    def test_book_list_view(self):
        response = self.client.get(reverse('books:book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_detail_view(self):
        response = self.client.get(reverse('books:book_detail', args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

