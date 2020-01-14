from django.urls import path
from . import views

urlpatterns = [
    path('all_members', views.all_members, name='all_members'),
    path('search', views.search, name='search_member'),
    path('<int:member_id>', views.member, name='member'),
]