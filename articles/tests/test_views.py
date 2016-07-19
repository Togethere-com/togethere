from django.test import TestCase
from django.contrib.auth.models import User

from articles.views import articles
from articles.models import Article

class HomePageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'articles/articles.html')

    def test_home_page_displays_articles(self):
        first_article = Article.objects.create(title='foo',text='bla bla bla',author=self.user)
        second_article = Article.objects.create(title='bar',text='bla bla bla bla',author=self.user)
        response = self.client.get('/')
        self.assertContains(response, 'foo')
        self.assertContains(response, 'bar')
