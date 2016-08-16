from django.contrib import admin
from .models import Article, Category, City, Profile

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Profile)
