from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=('id','name', 'is_current')
    list_display_links=('id', 'name')
    search_fields=('name',)
    list_per_page=(10)
    list_editable=('is_current',)

admin.site.register(Member, MemberAdmin)