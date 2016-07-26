from django.db import models

class Category(models.Model):
    GENERAL_INFORMATION = 'GEN'
    FOOD_AND_DRINKS = 'FOO'
    SLEEPING = 'SLE'
    CULTURE = 'CUL'
    OUTSIDE = 'OUT'
    TRANSPORT = 'TRA'
    STAYING_SAFE = 'STA'
    CATEGORY_CHOICES = (
        (GENERAL_INFORMATION, 'General information'),
        (FOOD_AND_DRINKS, 'Food and drinks'),
        (SLEEPING, 'Sleeping'),
        (CULTURE, 'Culture'),
        (OUTSIDE, 'Outside'),
        (TRANSPORT, 'Transport'),
        (STAYING_SAFE, 'Staying safe'),
    )
    name = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default=GENERAL_INFORMATION,
        blank=False,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
