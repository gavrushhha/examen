from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    author1 = forms.ModelChoiceField(queryset=Author.objects.all(), label='Author 1')
    author2 = forms.ModelChoiceField(queryset=Author.objects.all(), label='Author 2')

    class Meta:
        model = Book
        fields = ('title', 'description', 'genre', 'year')

    def save(self, commit=True):
        book = super().save(commit=False)
        book.save()

        author1 = self.cleaned_data.get('author1')
        author2 = self.cleaned_data.get('author2')

        book.authors.add(author1)
        book.authors.add(author2)

        if commit:
            book.save()

        return book
