from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *
from .models import Article

urlpatterns = [
    url(r'^$', ArticlesView.as_view(model=Article), name='articles'),
    url(r'^(?P<pk>\d+)/?$', ArticleView.as_view(), name='article'),
    url(r'^article-submit/$', login_required(ArticleSubmitView.as_view()), name='article-submit'),
    url(r'^article-update/(?P<pk>\d+)/$', login_required(ArticleUpdateView.as_view()), name='article-update'),
    url(r'^article-delete/(?P<pk>\d+)/$', login_required(ArticleDeleteView.as_view()), name='article-delete'),
    url(r'^article-like/(?P<article_id>\d+)/$', login_required(ArticleLikeView), name='article-like'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='profile'),
]
