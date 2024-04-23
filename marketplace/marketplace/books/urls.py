from django.urls import path
from .views import BookCreateView, BookListView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('list/', BookListView.as_view(), name='book_list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]