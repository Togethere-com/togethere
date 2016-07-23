from django.shortcuts import render, get_object_or_404

from .models import Article
from .forms import ArticleForm

# Create your views here.
def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles, 'form': ArticleForm})

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html', {'article': article})
