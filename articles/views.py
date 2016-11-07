from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Article, Category, City, Profile
from .forms import ArticleForm

class ArticlesView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 25
    template_name = 'articles/articles.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlesView, self).get_context_data(**kwargs)
        context['form'] = ArticleForm
        return context

class ArticleView(DetailView):
    model = Article
    template_name = 'articles/article.html'

class ArticleSubmitView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article-submit.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(reverse('article', kwargs={'pk': obj.id}))

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name_suffix = '-update'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(reverse('article', kwargs={'pk': obj.id}))

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles')
    template_name_suffix = '-delete'

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
        context = super(CityView, self).get_context_data(**kwargs)
        context['city'] = City.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Article.objects.filter(city=self.kwargs['pk'])

    template_name = 'articles/city.html'

class ProfileView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 25
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Article.objects.filter(author__id=self.kwargs['pk'])

    template_name = 'articles/profile.html'
