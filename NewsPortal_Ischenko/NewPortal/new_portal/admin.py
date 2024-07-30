from django.contrib import admin
from .models import Category, Post

def nullfy_quantity(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)
nullfy_quantity.short_description = 'Обнулить товары' # описание для более понятного представления в админ панеле задаётся, как будто это объект

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'category', 'date_creation')
    list_filter = ('date_creation', 'category', 'name')
    search_fields = ('name', 'category__name')

admin.site.register(Category)
admin.site.register(Post)