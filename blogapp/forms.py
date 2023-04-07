from django import forms
from .models import Blog


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'subtitle', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),

        }
