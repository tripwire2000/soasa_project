from django.contrib import admin
from .models import NewsItem
# Register your models here.

class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    list_display_links = ('title', 'photo')
    list_per_page = 15

admin.site.register(NewsItem, NewsItemAdmin)