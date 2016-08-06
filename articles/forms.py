from django import forms
from django.forms import ModelForm

from .models import Article, Category, City

TITLE_LENGTH_ERROR = "This title is too long, please make it 200 characters or less."
TITLE_EMPTY_ERROR = "You’ll have to add a title."
TEXT_EMPTY_ERROR = "Please enter some text."
NO_CATEGORY_ERROR = "Please select a category."
NO_CITY_ERROR = "Please select a city."


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'categories', 'city']
        widgets = {'title': forms.TextInput(attrs={
            'placeholder': 'Enter a descriptive title'}),
            'text': forms.Textarea(attrs={'placeholder': 'The article'}),
            'categories': forms.CheckboxSelectMultiple(choices=Category.CATEGORY_CHOICES),
            'city': forms.RadioSelect(choices=City.CITY_CHOICES),
        }
        error_messages = {
            'title': {
                'max_length': TITLE_LENGTH_ERROR,
                'required': TITLE_EMPTY_ERROR,
            },
            'text': {
                'required': TEXT_EMPTY_ERROR,
            },
            'categories': {
                'required': NO_CATEGORY_ERROR,
            },
            'city': {
                'required': NO_CITY_ERROR,
            }
        }
