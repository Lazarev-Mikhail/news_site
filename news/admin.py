from django.contrib import admin
from .models import Category, News


# Register your models here.

@admin.register(News)  # привязка при помощи декоратора
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'time']
    ordering = ['-time']
    list_per_page = 10
    search_fields = ['name__startwith']
    prepopulated_fields = {'slug_news': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
