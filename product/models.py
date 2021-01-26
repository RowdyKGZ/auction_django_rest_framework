import uuid
from time import time

from django.contrib.auth import get_user_model
from django.db import models
from pytils.translit import slugify


def get_slug(s):
    """Генерация слага по названию"""
    slug = slugify(s)
    return slug + '-' + str(int(time()))


class Category(models.Model):
    """Клас категории"""
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, primary_key=True, blank=True)

    # Подкласс категории
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = get_slug(self.name)
        super().save()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """Продукт"""
    uuid = models.UUIDField(primary_key=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('price',)


class ProductImage(models.Model):
    """Каритнки к продукту"""
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)


class Comment(models.Model):
    """Коменты к продукту"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Коментарий {self.author} для {self.product}, создан {self.create_at}'
