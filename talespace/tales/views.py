from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Tale


def index(request):
    context = {
        # 'tales_list': tales_list,
    }
    return render(request, 'tales/index.html', context)
    # return HttpResponse("Hello, world! You're at the tales index.")


def tales_list(request):
    # tales_list = Tale.objects
    # return render(request, 'tales/tales_list.html', {})
    return HttpResponse("This is the Tales List Page!")

def tale_details(request, tale_id):
    # return render(request, 'tales/tale_details.html', {})
    return HttpResponse("This is the Tale Details Page --> %s!" % tale_id)

def user_details(request, user_id):
    user = User.object
    return render(request, 'tales/user_profile.html', {'user': user})
    # return HttpResponse("This is the User Details Page --> %s!" % user_id)
