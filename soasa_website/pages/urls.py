from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('<int:news_id>', views.single_news_item, name='single_news'),
    path('about', views.about, name='about'),
    #path('search', views.search, name='search'),
]