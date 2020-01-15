from django.shortcuts import render, get_object_or_404
from members.models import Member
from courses.models import Course
from .models import NewsItem

# Create your views here. 
def index(request):
    members = Member.objects.filter(is_current=True)[:4]
    courses = Course.objects.all()[:4]  

    context = {
        'members':members,
        'courses':courses
    }
    return render(request, 'pages/index.html', context)

def news(request):
    all_news = NewsItem.objects.all()[:5]

    context = {
        'all_news':all_news
    }
    return render(request, 'pages/news.html', context)

def single_news_item(request, news_id):
        news = get_object_or_404(NewsItem, pk=news_id)

        context = {
            'news':news 
        }

        return render(request, 'pages/single_news.html', context)



def about(request):
    return render(request, 'pages/about.html')

'''
def search(request):
    all_courses = Course.objects.all()

    if 'search' in request.GET:
        searchterm = request.GET['search']
        if searchterm:
            allcourses = allcourses.filter(title__icontains=searchterm)

    context = {
        'allcourses':allcourses
    }
'''