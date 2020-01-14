from django.urls import path
from . import views

urlpatterns = [
    path('courses_all', views.courses_all, name='courses_all'),
    path('search', views.search, name='search'),
    path('<int:course_id>', views.course, name='course'),
]