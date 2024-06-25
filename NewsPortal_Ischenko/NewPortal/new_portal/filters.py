from django_filters import FilterSet, ModelChoiceFilter
from .models import Post


class PostFilter(FilterSet):

   class Meta:
       model = Post
       fields = {
           # поиск по названию
           'name': ['icontains'],
           'description': ['icontains'],
           'date_creation': ['gt']
       }