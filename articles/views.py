from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Article, Category, City
from .forms import ArticleSubmitForm

class ArticlesView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 25
    template_name = 'articles/articles.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlesView, self).get_context_data(**kwargs)
        context['form'] = ArticleSubmitForm(auto_id=True)
        return context

class ArticleView(DetailView):
    model = Article
    template_name = 'articles/article.html'

class ArticleSubmitView(CreateView):
    pass

class ArticleUpdateView(UpdateView):
    pass

class ArticleDeleteView(DeleteView):
    pass

class CategoriesView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'articles/categories.html'

class CategoryView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 25
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryView, self).get_context_data(**kwargs)
        # Add in a QuerySet of the category
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Article.objects.filter(categories=self.kwargs['pk'])

    template_name = 'articles/category.html'

class CitiesView(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'articles/cities.html'

class CityView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 25
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CityView, self).get_context_data(**kwargs)
        # Add in a QuerySet of the city
        context['city'] = City.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Article.objects.filter(cities=self.kwargs['pk'])

    template_name = 'articles/city.html'
