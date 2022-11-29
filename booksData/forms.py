from django import forms
from booksData.models import Library

class BooksForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = "__all__"