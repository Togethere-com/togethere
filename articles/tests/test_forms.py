from django.contrib.auth.models import User
from django.test import TestCase

from articles.models import Article, Category, City
from articles.forms import (
    ArticleForm,
    CategoryForm,
    CityForm,
    TITLE_LENGTH_ERROR,
    TITLE_EMPTY_ERROR,
    TEXT_EMPTY_ERROR,
    NO_CATEGORY_ERROR,
    NO_CITY_ERROR,
)


class ArticleFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_form_item_input_has_placeholder(self):
        form = ArticleForm()
        self.assertIn('placeholder="Enter a descriptive title"', form.as_p())

    def test_form_validation_for_blank_titles_and_text(self):
        form = ArticleForm(data={'title': '', 'text': '', 'author': self.user})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            [TITLE_EMPTY_ERROR]
        )
        self.assertEqual(
            form.errors['text'],
            [TEXT_EMPTY_ERROR]
        )

    def test_form_validation_for_too_long_titles(self):
        form = ArticleForm(data={'title': 'An unexpected failure—it’s actually in the tests for our final view, view_list. Because we’ve changed the way errors are displayed in all templates, we’re no longer showing the error that we manually pass into the template.', 'text': 'bla bla', 'author': self.user})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            [TITLE_LENGTH_ERROR]
        )

class CategoryFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_form_validation_for_blank_category(self):
        form = CategoryForm(data={'category': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['name'],
            [NO_CATEGORY_ERROR]
        )

class CityFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_form_validation_for_blank_city(self):
        form = CityForm(data={'city': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['name'],
            [NO_CITY_ERROR]
        )
