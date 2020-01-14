from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'course_code', 'level')
    list_display_links=('id', 'name')
    search_fields=('name','course_code', 'level')
    list_per_page=(10)

admin.site.register(Course, CourseAdmin)