from collections import OrderedDict

from django import forms
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm

from .models import Article, Category

TITLE_LENGTH_ERROR = "This title is too long, please make it 140 characters or less."
TITLE_EMPTY_ERROR = "You’ll have to add a title."
TEXT_EMPTY_ERROR = "Please enter some text."
NO_CATEGORY_ERROR = "Please select at least one category"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Category'
        }
        widgets = {
            'name': forms.CheckboxSelectMultiple()
        }
        error_messages = {
            'name': {
                'required': NO_CATEGORY_ERROR,
            }
        }

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

class ArticleSubmitForm(MultiModelForm):
    form_classes = OrderedDict((
        ('article', ArticleForm),
        ('category', CategoryForm),
    ))
    class Meta:
        fieldsets = (
            ('article', {'fields': ('title', 'text',)}),
            ('category', {'fields': ('name',)}),
        )
