from django.shortcuts import render, get_object_or_404
from .models import Member
from django.http import HttpResponse

# Create your views here.
def all_members(request):
    current_members = Member.objects.filter(is_current=True)
    past_members = Member.objects.filter(is_current=False)

    context = {
        'current_members':current_members,
        'past_members':past_members
    }
    return render(request, 'members/all_members.html', context)

def member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)

    context = {
        'member':member
    }
    return render(request, 'members/member.html', context)

def search(request):
    all_members = Member.objects.all()

    if 'search' in request.GET:
        searchterm = request.GET['search']
        if searchterm:
            all_members = all_members.filter(name__icontains=searchterm)
        else:
            return HttpResponse('please enter a name to search')

    context= {
        'all_members':all_members
    }
    return render(request, 'members/members_results.html', context)