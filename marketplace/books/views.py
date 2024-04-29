from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .forms import BookForm
from .models import Book
from django.urls import reverse_lazy
from drf_yasg.utils import swagger_auto_schema

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books:book_list')

    @swagger_auto_schema(operation_summary="Create a new book")
    def post(self, request, *args, **kwargs):
        """
        Создает новую книгу.
        
        ---
        parameters:
          - name: title
            type: string
            description: Название книги.
            required: true
          - name: authors
            type: array
            description: Список авторов книги.
            required: true
          - name: genre
            type: string
            description: Жанр книги.
            required: true
        responses:
          200:
            description: Книга успешно создана.
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    @swagger_auto_schema(operation_summary="List all books")
    def get(self, request, *args, **kwargs):
        """
        Показывает список книг.
        
        ---
        responses:
          200:
            description: Список книг успешно получен.
        """
        return super().get(request, *args, **kwargs)


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    @swagger_auto_schema(operation_summary="Retrieve a book")
    def get(self, request, *args, **kwargs):
        """
        Показывает детали книги.
        
        ---
        parameters:
          - name: id
            type: integer
            description: Идентификатор книги.
            required: true
        responses:
          200:
            description: Детали книги успешно получены.
        """
        return super().get(request, *args, **kwargs)
