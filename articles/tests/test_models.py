from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from articles.models import Article, Category, City, Profile

class ArticleModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_can_create_article(self):
        amsterdam = City.objects.create(name='AMS')
        article = Article.objects.create(title='Article Title',text='Article text',author=self.user,city=amsterdam)
        self.assertEqual(Article.objects.count(), 1)

    def test_empty_articles_not_allowed(self):
        amsterdam = City.objects.create(name='AMS')
        article = Article.objects.create(title='',text='',author=self.user,city=amsterdam)
        with self.assertRaises(ValidationError):
            article.full_clean()
            article.save()

    def test_article_score(self):
        amsterdam = City.objects.create(name='AMS')
        rotterdam = City.objects.create(name='ROT')
        first_article = Article.objects.create(
            title='First Article Title',
            text='First article text',
            author=self.user,
            city=amsterdam,
            score=1
        )
        second_article = Article.objects.create(
            title='Second Article Title',
            text='Second article text',
            author=self.user,
            city=rotterdam,
            score=2
        )
        self.assertGreater(second_article.score, first_article.score)
        first_article.score = 3
        first_article.save()
        self.assertEqual(first_article.score, 3)
        self.assertGreater(first_article.score, second_article.score)

class CategoryModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_can_create_category(self):
        Category.objects.create(name='GEN')
        self.assertEqual(Category.objects.count(), 1)


class CityModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_can_create_city(self):
        City.objects.create(name='AMS')
        self.assertEqual(City.objects.count(), 1)

class CategoryAndCityModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_can_associate_category_and_city_to_article(self):
        general_information = Category.objects.create(name='GEN')
        food_and_drinks = Category.objects.create(name='FOO')
        amsterdam = City.objects.create(name='AMS')
        article = Article.objects.create(title='Article Title',text='Article text',author=self.user,city=amsterdam)
        article.categories.add(general_information, food_and_drinks)

        self.assertEqual(article.city, amsterdam)
        self.assertListEqual(list(article.categories.values_list('id', flat=True)), [1, 2])

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_can_create_profile(self):
        #profile should already be there when user is created
        self.assertEqual(Profile.objects.count(), 1)
