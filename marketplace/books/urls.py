from django.urls import path
from .views import BookCreateAPIView, BookListAPIView, BookDetailAPIView

app_name = 'books'

urlpatterns = [
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
    path('list/', BookListAPIView.as_view(), name='book_list'),
    path('detail/<int:pk>/', BookDetailAPIView.as_view(), name='book_detail'),
]
