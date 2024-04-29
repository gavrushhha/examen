from django.urls import path
from .views import BookCreateView, BookListView, BookDetailView

app_name = 'books'

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title = "Books API", 
        default_version='1.0.0', 
        description="Api documentation for app", 
    ), 
    public=True, 
)

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('list/', BookListView.as_view(), name='book_list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")
]