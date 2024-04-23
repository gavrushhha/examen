from django.contrib import admin
from .models import Book
from .models import Author

admin.site.register(Book)
admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    actions = ['approve_books', 'reject_books']

    def approve_books(self, request, queryset):
        queryset.update(status='approved')

    def reject_books(self, request, queryset):
        queryset.update(status='rejected')

    approve_books.short_description = 'Approve selected books'
    reject_books.short_description = 'Reject selected books'