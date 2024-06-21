from django_filters import FilterSet, ModelChoiceFilter
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):

   class Meta:
       model = Post
       fields = {
           # поиск по названию
           'name': ['icontains'],
           'description': ['icontains']
       }