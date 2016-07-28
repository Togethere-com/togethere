from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^(?P<article_id>[0-9]+)/?$', views.article, name='article'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'category/(?P<category_id>[0-9]+)', views.category, name='category'),
    url(r'^cities/$', views.cities, name='cities'),
    url(r'city/(?P<city_id>[0-9]+)', views.city, name='city'),
]
