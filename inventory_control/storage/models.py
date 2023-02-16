from django.contrib.auth.models import User
from django.db import models


class Goods(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва')
    content = models.TextField(blank=True, verbose_name='Опис')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час змінення')
    is_published = models.BooleanField(default=False, verbose_name='Публікація')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорія')
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    '''def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})'''


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    '''def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})'''
