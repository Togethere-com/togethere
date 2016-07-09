from django.test import TestCase
from django.contrib.auth.models import User

from articles.views import articles
from articles.models import Article

class HomePageTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'articles/articles.html')

    def test_home_page_displays_articles(self):
        first_article = Article.objects.create(title='foo',text='bla bla bla')
        second_article = Article.objects.create(title='bar',text='bla bla bla bla')
        response = self.client.get('/')
        self.assertContains(response, 'foo')
        self.assertContains(response, 'bar')
