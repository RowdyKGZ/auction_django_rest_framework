from django.contrib import admin

from .models import Category, Product, ProductImage, Comment


class ImageInline(admin.TabularInline):
    """подключить инлайново картинки к продукту в админке"""
    model = ProductImage
    extra = 2
    fields = ('image',)


class CommentInLine(admin.TabularInline):
    """подключить инлайново коментарии к продукту в админке"""
    model = Comment
    extra = 3
    fields = ('comment',)


class ProductAdmin(admin.ModelAdmin):
    """Продукт в админке инлайново"""
    inlines = [ImageInline, CommentInLine]
    list_display = ('title', 'uuid', 'price')
    list_display_links = ('uuid', 'title')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
