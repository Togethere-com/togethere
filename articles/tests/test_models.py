from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from articles.models import Article, Category

class ArticleModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_can_create_article(self):
        article = Article.objects.create(title='Article Title',text='Article text',author=self.user)
        self.assertEqual(Article.objects.count(), 1)

    def test_empty_articles_not_allowed(self):
        article = Article.objects.create(title='',text='',author=self.user)
        with self.assertRaises(ValidationError):
            article.full_clean()
            article.save()

class CategoryModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_can_create_category(self):
        category = Category.objects.create(name='GEN')
        self.assertEqual(Category.objects.count(), 1)

    def test_associate_category_to_article(self):
        general_information = Category.objects.create(name='GEN')
        article = Article.objects.create(title='Article Title',text='Article text',author=self.user)
        article.categories.add(general_information)
        self.assertIn(general_information, article.categories.all())
