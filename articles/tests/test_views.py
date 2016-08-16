from django.test import TestCase
from django.contrib.auth.models import User

from articles.views import ArticlesView, ArticleView, CategoriesView, CategoryView, CitiesView, CityView, ArticleSubmitView, ArticleUpdateView, ArticleDeleteView
from articles.models import Article, Category, City

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
        amsterdam = City.objects.create(name='AMS')
        first_article = Article.objects.create(title='foo',text='bla bla bla',author=self.user,city=amsterdam)
        second_article = Article.objects.create(title='bar',text='bla bla bla bla',author=self.user,city=amsterdam)
        response = self.client.get('/')
        self.assertContains(response, 'foo')
        self.assertContains(response, 'bar')

    def test_articles_pagination(self):
        amsterdam = City.objects.create(name='AMS')
        for i in range(27):
            i = Article.objects.create(title='title number {0}'.format(i),text='bla bla bla time {0}'.format(i),author=self.user,city=amsterdam)
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
        amsterdam = City.objects.create(name='AMS')
        rotterdam = City.objects.create(name='ROT')
        first_article = Article.objects.create(title='foo',text='bla bla bla',author=self.user,city=amsterdam)
        general_information = Category.objects.create(name='GEN')
        food_and_drinks = Category.objects.create(name='FOO')
        first_article.categories.add(general_information)

    def test_article_page(self):
        response = self.client.get('/1/')
        self.assertTemplateUsed(response, 'articles/article.html')
        self.assertContains(response, 'foo')

    def test_can_submit_article(self):
        response = self.client.post('/article-submit/', data={
            'title': 'Test title',
            'text': 'Test text',
            'categories': [1],
            'city': 1,
            'author': self.user,
            })
        self.assertEqual(Article.objects.all().count(), 2)
        self.assertRedirects(response, '/2')

    def test_can_update_article(self):
        response = self.client.post('/article-update/1/', data={
            'title': 'Edited title',
            'text': 'Edited text',
            'categories': [1, 2],
            'city': 2,
            'author': self.user,
            })
        self.assertRedirects(response, '/1')
        updated_article = Article.objects.get(pk=1)
        updated_city = City.objects.get(pk=2)
        self.assertEqual(updated_article.city, updated_city)
        self.assertEqual(updated_article.categories.count(), 2)
        self.assertListEqual(list(updated_article.categories.values_list('id', flat=True)), [1, 2])

        new_page = self.client.get('/1/')
        self.assertContains(new_page, "Edited title")

    def test_can_delete_article(self):
        response = self.client.post('/article-delete/1/')
        self.assertEqual(Article.objects.all().count(), 0)

    def test_validation_errors_are_sent_to_submit_view(self):
        response = self.client.post('/article-submit/', data={'title': '', 'text': '', 'categories': '', 'city':''})
        self.assertEqual(Article.objects.all().count(), 1)
        self.assertTemplateUsed(response, 'articles/article-submit.html')
        expected_error = "You’ll have to add a title."
        self.assertContains(response, expected_error)

class CategoriesPageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')
        amsterdam = City.objects.create(name='AMS')
        article = Article.objects.create(title='foo',text='bla bla bla',author=self.user,city=amsterdam)
        general_information = Category.objects.create(name='GEN')
        article.categories.add(general_information)

    def test_categories_page(self):
        response = self.client.get('/categories/')
        self.assertTemplateUsed(response, 'articles/categories.html')
        self.assertContains(response, 'General information')

class CategoryPageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')
        amsterdam = City.objects.create(name='AMS')
        article = Article.objects.create(title='foo',text='bla bla bla',author=self.user,city=amsterdam)
        general_information = Category.objects.create(name='GEN')
        article.categories.add(general_information)

    def test_category_page(self):
        response = self.client.get('/category/1/')
        self.assertTemplateUsed(response, 'articles/category.html')
        self.assertContains(response, 'General information')

class CitiesPageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')
        amsterdam = City.objects.create(name='AMS')
        article = Article.objects.create(title='foo',text='bla bla bla',author=self.user,city=amsterdam)

    def test_cities_page(self):
        response = self.client.get('/cities/')
        self.assertTemplateUsed(response, 'articles/cities.html')
        self.assertContains(response, 'Amsterdam')

class CityPageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')
        amsterdam = City.objects.create(name='AMS')
        article = Article.objects.create(title='foo',text='bla bla bla',author=self.user,city=amsterdam)

    def test_city_page(self):
        response = self.client.get('/city/1/')
        self.assertTemplateUsed(response, 'articles/city.html')
        self.assertContains(response, 'Amsterdam')

class ProfilePageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_profile_page_and_association_with_article(self):
        second_user = User.objects.create(username='testuser2')
        second_user.set_password('0987654')
        second_user.save()

        general_information = Category.objects.create(name='GEN')
        food_and_drinks = Category.objects.create(name='FOO')
        amsterdam = City.objects.create(name='AMS')
        rotterdam = City.objects.create(name='ROT')
        first_article = Article.objects.create(
            title='Article Title 1',
            text='Article text 1',
            author=self.user,
            city=amsterdam
        )
        first_article.categories.add(general_information)

        second_article = Article.objects.create(
            title='Article Title 2',
            text='Article text 2',
            author=second_user,
            city=rotterdam
        )
        second_article.categories.add(food_and_drinks)

        first_response = self.client.get('/profile/1/')
        self.assertTemplateUsed(first_response, 'articles/profile.html')
        self.assertContains(first_response, 'Article Title 1')

        second_response = self.client.get('/profile/2/')
        self.assertContains(second_response, 'Article Title 2')
