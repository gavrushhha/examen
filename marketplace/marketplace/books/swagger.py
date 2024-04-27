from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from .views import BookCreateView, BookListView, BookDetailView

class MyAutoSchema(SwaggerAutoSchema):
    def get_request_serializer(self):
        return self._get_serializer('request')

    def get_response_serializer(self):
        return self._get_serializer('response')

    def _get_serializer(self, direction):
        if direction == 'request':
            return getattr(self.view, 'request_serializer', None)
        return getattr(self.view, 'response_serializer', None)

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for Your Project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
    generator_class=MyAutoSchema
)
