from django.conf.urls import url
# from . import views
from .views import ArticlesView, ArticleView, CategoriesView, CategoryView, CitiesView, CityView

urlpatterns = [
    url(r'^$', ArticlesView.as_view(), name='articles'),
    url(r'^(?P<pk>\d+)/?$', ArticleView.as_view(), name='article'),
    url(r'^categories/$', CategoriesView.as_view(), name='categories'),
    url(r'^category/(?P<pk>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^cities/$', CitiesView.as_view(), name='cities'),
    url(r'^city/(?P<pk>\d+)/$', CityView.as_view(), name='city'),
]
