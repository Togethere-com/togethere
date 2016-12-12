from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy

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
        return self.get_name_display()

class City(models.Model):
    AMSTERDAM = 'AMS'
    ROTTERDAM = 'ROT'
    THE_HAGUE = 'THE'
    UTRECHT = 'UTR'
    CITY_CHOICES = (
        (AMSTERDAM, 'Amsterdam'),
        (ROTTERDAM, 'Rotterdam'),
        (THE_HAGUE, 'The Hague'),
        (UTRECHT, 'Utrecht'),
    )
    name = models.CharField(
        max_length=3,
        choices=CITY_CHOICES,
        default=AMSTERDAM,
        blank=False,
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.get_name_display()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    categories = models.ManyToManyField(Category)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article', kwargs={'pk': self.id})
