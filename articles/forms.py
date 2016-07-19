from django import forms
from django.forms import ModelForm

from .models import Article

TITLE_LENGTH_ERROR = "This title is too long, please make it 140 characters or less."
TITLE_EMPTY_ERROR = "You’ll have to add a title."
TEXT_EMPTY_ERROR = "Please enter some text."

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a descriptive title'}),
            'article': forms.Textarea(attrs={'placeholder': 'The article'}),
        }
        error_messages = {
            'title': {
                'max_length': TITLE_LENGTH_ERROR,
                'required': TITLE_EMPTY_ERROR,
            },
            'text': {
                'required': TEXT_EMPTY_ERROR,
            }
        }
