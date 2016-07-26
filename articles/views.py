from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Category
from .forms import ArticleSubmitForm

# Create your views here.
def articles(request):
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 25) # Show 25 articles per page

    page = request.GET.get('page')

    form = ArticleSubmitForm(auto_id=True)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles/articles.html', {'articles': articles, 'form': form})

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html', {'article': article})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'articles/categories.html', {'categories': categories})

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    all_articles = Article.objects.filter(categories=category_id)
    paginator = Paginator(all_articles, 25) # Show 25 articles per page

    page = request.GET.get('page')

    form = ArticleSubmitForm(auto_id=True)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles/category.html', {'category': category, 'articles': articles})
