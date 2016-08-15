from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ArticlesView.as_view(), name='articles'),
    url(r'^(?P<pk>\d+)/?$', ArticleView.as_view(), name='article'),
    url(r'^categories/$', CategoriesView.as_view(), name='categories'),
    url(r'^category/(?P<pk>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^cities/$', CitiesView.as_view(), name='cities'),
    url(r'^city/(?P<pk>\d+)/$', CityView.as_view(), name='city'),
    url(r'^article-submit/$', ArticleSubmitView.as_view(), name='article-submit'),
    url(r'^article-update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='article-update'),
    url(r'^article-delete/(?P<pk>\d+)/$', ArticleDeleteView.as_view(), name='article-delete'),
]
