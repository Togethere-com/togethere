from django.shortcuts import render

from .models import Article
from .forms import ArticleForm

# Create your views here.
def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles, 'form': ArticleForm})
