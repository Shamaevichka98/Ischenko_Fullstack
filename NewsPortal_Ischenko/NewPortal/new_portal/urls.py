from django.urls import path, include
from django.contrib import admin
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch, subscriptions
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    # path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('<int:pk>/', cache_page(60 * 10)(PostDetail.as_view()), name='post_detail'),# добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.
]