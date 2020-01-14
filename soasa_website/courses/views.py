from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.
def courses_all(request):
    level_100_courses = Course.objects.filter(level=100)
    level_200_courses = Course.objects.filter(level=200)
    level_300_courses = Course.objects.filter(level=300)
    level_400_courses = Course.objects.filter(level=400)

    context = {
        'level_100_courses':level_100_courses,
        'level_200_courses':level_200_courses,
        'level_300_courses':level_300_courses,
        'level_400_courses':level_400_courses
    }
    return render(request, 'courses/courses_all.html', context)

def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course':course
    }
    return render(request, 'courses/course.html', context)

def search(request):
    all_courses = Course.objects.all()

    if 'search' in request.GET:
        searchterm = request.GET['search']
        if searchterm:
            all_courses = all_courses.filter(name__icontains=searchterm)


    context = {
        'all_courses':all_courses,
        'values':request.GET
    }
    return render(request, 'courses/course_results.html', context)