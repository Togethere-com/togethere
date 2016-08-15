from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
import sys

from articles.models import Article, Category, City

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@email.com')
        self.user.set_password('1234567')
        self.user.save()
        amsterdam = City.objects.create(name='AMS')
        rotterdam = City.objects.create(name='ROT')
        first_article = Article.objects.create(title='foo',text='bla bla bla',city=amsterdam,author=self.user)
        second_article = Article.objects.create(title='bar',text='bla bla bla bla',city=rotterdam,author=self.user)
        general_information = Category.objects.create(name='GEN')
        food_and_drinks = Category.objects.create(name='FOO')
        first_article.categories.add(general_information)
        second_article.categories.add(food_and_drinks)
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
