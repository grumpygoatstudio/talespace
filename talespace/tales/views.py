from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Tale


def index(request):
    context = {
        # 'tales_list': tales_list,
    }
    return render(request, 'tales/index.html', context)

def tales_list(request):
    # tales_list = Tale.objects
    # return render(request, 'tales/tales_list.html', {})
    return HttpResponse("This is the Tales List Page!")

def tale_details(request, tale_id):
    tale = Tale.objects.get(id=int(tale_id))
    context = {
        'tale': tale, 
        'author_name': tale.author.get_full_name(),
        # 'author_country': tale.author.country
    }
    return render(request, 'tales/tale_details.html', context)
    # return HttpResponse("This is the Tale Details Page --> %s!" % tale_id)

def user_profile(request, user_id):
    if request.user.is_authenticated():
        context = {
            'user': request.user,
        }
        return render(request, 'tales/user_profile.html', context)
    else:
        return HttpResponse("User is not logged in or does not match attempted Profile ID --> %s!" % user_id)