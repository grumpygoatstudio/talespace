from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Author, Tale


def index(request):
    tales = Tale.objects.all()
    context = {
        'tales': tales,
    }
    return render(request, 'tales/index.html', context)

def tales_list(request):
    tales = Tale.objects.all()
    context = {
        'tales': tales,
    }
    return render(request, 'tales/tales_list.html', context)

def tale_details(request, tale_id):
    tale = Tale.objects.get(id=int(tale_id))
    context = {
        'tale': tale,
    }
    return render(request, 'tales/tale_details.html', context)

def user_profile(request, user_id):
    if request.user.is_authenticated():
        context = {
            'user': request.user,
        }
        return render(request, 'tales/user_profile.html', context)
    else:
        return HttpResponse("User is not logged in or does not match attempted Profile ID --> %s!" % user_id)
    