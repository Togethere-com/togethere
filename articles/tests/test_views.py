from django.test import TestCase
from django.contrib.auth.models import User

from articles.views import articles
from articles.models import Article

class ArticlesPageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_articles_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'articles/articles.html')

    def test_articles_page_displays_articles(self):
        first_article = Article.objects.create(title='foo',text='bla bla bla',author=self.user)
        second_article = Article.objects.create(title='bar',text='bla bla bla bla',author=self.user)
        response = self.client.get('/')
        self.assertContains(response, 'foo')
        self.assertContains(response, 'bar')

    def test_pagination(self):
        for i in range(27):
            i = Article.objects.create(title='title number {0}'.format(i),text='bla bla bla time {0}'.format(i),author=self.user)
        first_page = self.client.get('/')
        self.assertContains(first_page, "page 1 of")
        second_page = self.client.get('/?page=2')
        self.assertContains(second_page, "page 2 of")

class ArticlePageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')
        first_article = Article.objects.create(title='foo',text='bla bla bla',author=self.user)

    def test_article_page_renders_home_template(self):
        response = self.client.get('/1/')
        self.assertTemplateUsed(response, 'articles/article.html')

    def test_article_page_displays_article(self):
        response = self.client.get('/1/')
        self.assertContains(response, 'foo')
